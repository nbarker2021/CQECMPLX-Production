"""
Hierarchical Orchestrator — Enforces ONE-LEVEL-DOWN constraint.

Architecture:
  Level 0 (Orchestrator)
    └─ Spawns Level 1 (Paper Validators) at 50% resources
       └─ Each spawns Level 2 (Tool Runners) at 50% resources

Every child operates under parent constraints. No child can exceed 50%
of parent's allocation.

Usage:
  python -m cmplx_proof_kernel.orchestrator \
    --level 0 \
    --role orchestrator \
    --docker-socket /var/run/docker.sock \
    --network cqecmplx-kernel-net \
    --child-memory 2048 \
    --child-cpu 2.0 \
    --max-papers 8 \
    --serve
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import os
import sys
import time
import uuid
from dataclasses import dataclass, field, asdict
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse

import docker
from docker.models.containers import Container


# ============================================================================
# Configuration & Hierarchy
# ============================================================================

class OrchestratorLevel(Enum):
    """Orchestration hierarchy level."""
    LEVEL_0 = "orchestrator"  # Master kernel (4GB, 4 CPU)
    LEVEL_1 = "paper_validator"  # Paper validator (2GB, 2 CPU)
    LEVEL_2 = "tool_runner"  # Tool runner (1GB, 1 CPU)


@dataclass
class HierarchyConstraint:
    """Resource constraints for a hierarchy level."""
    level: int
    memory_mb: int
    cpu: float
    ulimit_nproc: int
    ulimit_nofile: int
    
    def child_constraints(self) -> HierarchyConstraint:
        """Compute 50% child constraints."""
        return HierarchyConstraint(
            level=self.level + 1,
            memory_mb=self.memory_mb // 2,
            cpu=self.cpu / 2,
            ulimit_nproc=self.ulimit_nproc // 2,
            ulimit_nofile=self.ulimit_nofile // 2,
        )


# ============================================================================
# Orchestrator State
# ============================================================================

@dataclass
class PaperValidationTask:
    """Single paper validation task."""
    paper_id: str
    task_id: str = field(default_factory=lambda: f"task-{uuid.uuid4().hex[:12]}")
    status: str = "pending"  # pending, running, completed, failed
    container_id: Optional[str] = None
    container_name: str = ""
    receipt: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    start_time: Optional[float] = None
    end_time: Optional[float] = None
    
    @property
    def duration_seconds(self) -> float:
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        elif self.start_time:
            return time.time() - self.start_time
        return 0.0


@dataclass
class OrchestratorState:
    """Global orchestrator state."""
    level: int
    role: str
    orchestrator_id: str = field(default_factory=lambda: f"orch-{uuid.uuid4().hex[:12]}")
    parent_docker_socket: str = "/var/run/docker.sock"
    network: str = "cqecmplx-kernel-net"
    constraints: HierarchyConstraint = field(default_factory=lambda: HierarchyConstraint(0, 4096, 4.0, 4096, 65536))
    active_tasks: Dict[str, PaperValidationTask] = field(default_factory=dict)
    completed_tasks: List[PaperValidationTask] = field(default_factory=list)
    start_time: float = field(default_factory=time.time)


# ============================================================================
# Hierarchical Orchestrator
# ============================================================================

class HierarchicalOrchestrator:
    """Manages paper validation with strict hierarchy enforcement."""
    
    def __init__(
        self,
        level: int = 0,
        role: str = "orchestrator",
        docker_socket: str = "/var/run/docker.sock",
        network: str = "cqecmplx-kernel-net",
        child_memory_mb: int = 2048,
        child_cpu: float = 2.0,
        max_concurrent: int = 8,
    ):
        self.level = level
        self.role = role
        self.docker_socket = docker_socket
        self.network = network
        self.max_concurrent = max_concurrent
        
        # Initialize constraints
        if level == 0:
            self.constraints = HierarchyConstraint(0, 4096, 4.0, 4096, 65536)
        elif level == 1:
            self.constraints = HierarchyConstraint(1, child_memory_mb, child_cpu, 2048, 32768)
        else:
            raise ValueError(f"Invalid level: {level}")
        
        self.state = OrchestratorState(
            level=level,
            role=role,
            constraints=self.constraints,
        )
        
        self.docker_client = docker.DockerClient(base_url=f"unix://{docker_socket}")
        
        logging.basicConfig(
            level=logging.INFO,
            format=f"[L{level}:{role}] %(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger = logging.getLogger(__name__)
    
    # =====================================================================
    # Orchestration
    # =====================================================================
    
    async def orchestrate_papers(
        self,
        paper_ids: List[str],
        token_string: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Orchestrate validation of multiple papers.
        
        Each paper runs in a Level 1 container (if Level 0) or Level 2
        container (if Level 1), with 50% of parent resources.
        """
        self.logger.info(f"Orchestrating {len(paper_ids)} papers (Level {self.level})")
        
        # Create tasks
        tasks = [
            PaperValidationTask(paper_id=pid)
            for pid in paper_ids
        ]
        
        # Process concurrently (up to max_concurrent)
        results = []
        for i in range(0, len(tasks), self.max_concurrent):
            batch = tasks[i:i+self.max_concurrent]
            self.logger.info(f"Processing batch {i//self.max_concurrent + 1} ({len(batch)} papers)")
            
            batch_results = await asyncio.gather(
                *[self._validate_paper(task, token_string) for task in batch]
            )
            results.extend(batch_results)
        
        # Compile results
        overall_receipt = {
            "orchestrator_id": self.state.orchestrator_id,
            "level": self.level,
            "papers_validated": len(paper_ids),
            "papers_passed": len([r for r in results if r.get("status") == "pass"]),
            "papers_failed": len([r for r in results if r.get("status") == "fail"]),
            "total_duration_seconds": time.time() - self.state.start_time,
            "results": results,
        }
        
        self.logger.info(f"Orchestration complete: {overall_receipt['papers_passed']} passed, {overall_receipt['papers_failed']} failed")
        return overall_receipt
    
    async def _validate_paper(
        self,
        task: PaperValidationTask,
        token_string: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Validate a single paper by spawning a child container."""
        self.logger.info(f"Validating {task.paper_id} (task: {task.task_id})")
        task.status = "running"
        task.start_time = time.time()
        
        try:
            # Spawn child container with 50% resources
            child_constraints = self.constraints.child_constraints()
            
            container = await self._spawn_child_container(
                paper_id=task.paper_id,
                constraints=child_constraints,
                token_string=token_string,
            )
            
            task.container_id = container.id
            task.container_name = container.name
            self.state.active_tasks[task.task_id] = task
            
            # Wait for completion
            receipt = await self._wait_for_completion(container)
            
            task.status = "completed"
            task.receipt = receipt
            
        except Exception as e:
            self.logger.error(f"Validation failed for {task.paper_id}: {e}")
            task.status = "failed"
            task.error = str(e)
        
        finally:
            task.end_time = time.time()
            self.state.completed_tasks.append(task)
            if task.task_id in self.state.active_tasks:
                del self.state.active_tasks[task.task_id]
        
        return {
            "paper_id": task.paper_id,
            "status": task.status,
            "duration_seconds": task.duration_seconds,
            "receipt": task.receipt,
            "error": task.error,
        }
    
    async def _spawn_child_container(
        self,
        paper_id: str,
        constraints: HierarchyConstraint,
        token_string: Optional[str] = None,
    ) -> Container:
        """
        Spawn a child container with strict resource constraints.
        
        The child operates ONE LEVEL DOWN:
        - Level 0 → Level 1 paper validator (50% resources)
        - Level 1 → Level 2 tool runner (50% resources)
        """
        child_level = self.level + 1
        container_name = f"cqecmplx-paper-{paper_id}-validator-{uuid.uuid4().hex[:8]}"
        
        self.logger.info(
            f"Spawning child container: {container_name} "
            f"(Level {child_level}, {constraints.memory_mb}MB, {constraints.cpu} CPU)"
        )
        
        # Compute grandchild constraints (for tools this validator might spawn)
        grandchild_constraints = constraints.child_constraints()
        
        # Environment for child
        env = {
            "KERNEL_LEVEL": str(child_level),
            "KERNEL_ROLE": "paper_validator" if child_level == 1 else "tool_runner",
            "PAPER_ID": paper_id,
            "KERNEL_MAX_MEMORY_MB": str(constraints.memory_mb),
            "KERNEL_MAX_CPU": str(constraints.cpu),
            "CHILD_LEVEL": str(child_level + 1),
            "CHILD_MEMORY_MB": str(grandchild_constraints.memory_mb),
            "CHILD_CPU": str(grandchild_constraints.cpu),
            "CHILD_ULIMIT_NPROC": str(grandchild_constraints.ulimit_nproc),
            "CHILD_ULIMIT_NOFILE": str(grandchild_constraints.ulimit_nofile),
            "DNA_VALIDATION_MODE": "paper",
            "ORCHESTRATOR_NETWORK": self.network,
        }
        
        if token_string:
            env["DNA_TOKEN_STRING"] = token_string
        
        # Host config with hierarchy enforcement
        host_config = self.docker_client.api.create_host_config(
            mem_limit=f"{constraints.memory_mb}m",
            memswap_limit=f"{constraints.memory_mb}m",
            cpu_quota=int(constraints.cpu * 100000),
            cpu_period=100000,
            ulimits=[
                docker.types.Ulimit(name="nproc", soft=constraints.ulimit_nproc, hard=constraints.ulimit_nproc),
                docker.types.Ulimit(name="nofile", soft=constraints.ulimit_nofile, hard=constraints.ulimit_nofile),
            ],
            volumes_from=[],
            network_mode=self.network,
            restart_policy={"Name": "on-failure", "MaximumRetryCount": 2},
        )
        
        # Volumes: mount docker socket (read-only for hierarchy)
        volumes = {
            "/var/run/docker.sock": {"bind": "/var/run/docker.sock", "mode": "ro"}
        }
        
        # Create container
        container = self.docker_client.containers.create(
            image="python-dev:complete-stack",
            name=container_name,
            environment=env,
            volumes=volumes,
            host_config=host_config,
            entrypoint=[
                "python", "-m", "cmplx_proof_kernel.paper_validator",
                "--level", str(child_level),
                "--paper-id", paper_id,
                "--docker-socket", "/var/run/docker.sock",
                "--max-child-memory", str(grandchild_constraints.memory_mb),
                "--max-child-cpu", str(grandchild_constraints.cpu),
            ]
        )
        
        container.start()
        self.logger.info(f"Child container started: {container_name} (ID: {container.id[:12]})")
        
        return container
    
    async def _wait_for_completion(self, container: Container, timeout_seconds: int = 3600) -> Dict[str, Any]:
        """Wait for child container to complete and extract receipt."""
        self.logger.info(f"Waiting for container {container.name} to complete...")
        
        start_time = time.time()
        while time.time() - start_time < timeout_seconds:
            container.reload()
            
            if container.status == "exited":
                exit_code = container.attrs["State"]["ExitCode"]
                
                # Extract receipt from logs
                logs = container.logs(stdout=True, stderr=True).decode("utf-8")
                receipt = self._extract_receipt_from_logs(logs)
                
                if exit_code == 0:
                    self.logger.info(f"Container {container.name} completed successfully")
                else:
                    self.logger.warning(f"Container {container.name} exited with code {exit_code}")
                    if not receipt:
                        receipt = {"status": "error", "exit_code": exit_code, "logs": logs[-500:]}
                
                # Clean up
                try:
                    container.remove()
                except Exception as e:
                    self.logger.warning(f"Failed to remove container: {e}")
                
                return receipt or {"status": "unknown"}
            
            await asyncio.sleep(1)
        
        self.logger.error(f"Container {container.name} timed out")
        container.kill()
        container.remove()
        
        return {"status": "timeout"}
    
    def _extract_receipt_from_logs(self, logs: str) -> Optional[Dict[str, Any]]:
        """Extract JSON receipt from container logs."""
        lines = logs.split("\n")
        for line in reversed(lines):
            if line.strip().startswith("{"):
                try:
                    return json.loads(line)
                except json.JSONDecodeError:
                    continue
        return None


# ============================================================================
# CLI Entry Point
# ============================================================================

async def main() -> int:
    parser = argparse.ArgumentParser(description="Hierarchical Proof Kernel Orchestrator")
    parser.add_argument("--level", type=int, default=0, help="Orchestration level (0, 1, 2)")
    parser.add_argument("--role", default="orchestrator", help="Role: orchestrator, paper_validator, tool_runner")
    parser.add_argument("--docker-socket", default="/var/run/docker.sock", help="Docker socket path")
    parser.add_argument("--network", default="cqecmplx-kernel-net", help="Docker network")
    parser.add_argument("--child-memory", type=int, default=2048, help="Child memory (MB)")
    parser.add_argument("--child-cpu", type=float, default=2.0, help="Child CPU cores")
    parser.add_argument("--max-papers", type=int, default=8, help="Max concurrent papers")
    parser.add_argument("--papers", nargs="*", default=[], help="Paper IDs to validate")
    parser.add_argument("--token-string", help="DNA token string")
    parser.add_argument("--serve", action="store_true", help="Serve HTTP API")
    
    args = parser.parse_args()
    
    orchestrator = HierarchicalOrchestrator(
        level=args.level,
        role=args.role,
        docker_socket=args.docker_socket,
        network=args.network,
        child_memory_mb=args.child_memory,
        child_cpu=args.child_cpu,
        max_concurrent=args.max_papers,
    )
    
    if args.serve:
        # Start HTTP API server (see operator_server.py)
        from cmplx_proof_kernel.operator_server import start_server
        await start_server(orchestrator, port=8765)
        return 0
    
    if args.papers:
        # Validate specific papers
        receipt = await orchestrator.orchestrate_papers(args.papers, args.token_string)
        print(json.dumps(receipt, indent=2))
        return 0 if receipt["papers_failed"] == 0 else 1
    
    # Default: validate all papers
    paper_ids = [f"CQE-paper-{i:02d}" for i in range(32)]
    receipt = await orchestrator.orchestrate_papers(paper_ids, args.token_string)
    print(json.dumps(receipt, indent=2))
    return 0 if receipt["papers_failed"] == 0 else 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
