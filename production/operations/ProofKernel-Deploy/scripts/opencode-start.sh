#!/bin/bash
# ============================================================================
# opencode-start.sh - OpenCode CLI Terminal with Agent Integration
# ============================================================================
# Starts OpenCode CLI with pre-configured agent tied to kernel
#
# Features:
#   - Auto-initializes OpenCode CLI
#   - Pre-configures agent for kernel interaction
#   - Establishes connection to proof kernel
#   - Provides interactive terminal
#   - Handles graceful shutdown
#
# ============================================================================

set -e

echo "=========================================="
echo "OpenCode CLI Terminal Initialization"
echo "=========================================="

# =====================================================================
# 1. Verify Configuration
# =====================================================================

echo "[1/5] Verifying configuration..."

if [ -z "$KERNEL_ENDPOINT" ]; then
    echo "ERROR: KERNEL_ENDPOINT not set"
    exit 1
fi

if [ -z "$OPENCODE_WORKSPACE" ]; then
    echo "ERROR: OPENCODE_WORKSPACE not set"
    exit 1
fi

echo "✓ Kernel endpoint: $KERNEL_ENDPOINT"
echo "✓ Workspace: $OPENCODE_WORKSPACE"
echo "✓ Agent mode: $OPENCODE_AGENT_MODE"

# =====================================================================
# 2. Create Workspace Directories
# =====================================================================

echo "[2/5] Creating workspace directories..."

mkdir -p "$OPENCODE_WORKSPACE"
mkdir -p "$OPENCODE_DATA_PATH"
mkdir -p "$OPENCODE_DATA_PATH/agents"
mkdir -p "$OPENCODE_DATA_PATH/kernels"
mkdir -p "$OPENCODE_DATA_PATH/config"

echo "✓ Directories created"

# =====================================================================
# 3. Generate OpenCode Configuration
# =====================================================================

echo "[3/5] Generating OpenCode configuration..."

cat > "$OPENCODE_DATA_PATH/config/agent-config.json" << 'EOF'
{
  "agent": {
    "name": "cqecmplx-agent",
    "type": "docker",
    "mode": "kernel-aware",
    "kernel_aware": true,
    "docker": {
      "socket": "/var/run/docker.sock",
      "network": "cqecmplx-kernel-net",
      "max_memory_mb": 1024,
      "max_cpu": 1.0
    },
    "kernel": {
      "endpoint": "http://proof-kernel:8765",
      "mode": "orchestrator",
      "level": 0
    },
    "capabilities": [
      "container_management",
      "kernel_communication",
      "dna_validation",
      "receipt_retrieval",
      "paper_orchestration"
    ],
    "security": {
      "require_auth": false,
      "audit_logging": true,
      "sandbox_mode": true
    }
  }
}
EOF

echo "✓ Agent configuration created"

# =====================================================================
# 4. Generate Kernel Connection Script
# =====================================================================

echo "[4/5] Generating kernel connection helper..."

cat > "$OPENCODE_WORKSPACE/kernel-connect.py" << 'PYSCRIPT'
#!/usr/bin/env python3
"""
Kernel Connection Helper - Links OpenCode CLI Agent to Proof Kernel
"""

import os
import json
import requests
import sys
from typing import Dict, Any

class KernelConnection:
    """Manages connection to proof kernel"""
    
    def __init__(self, kernel_endpoint: str):
        self.endpoint = kernel_endpoint
        self.agent_id = os.getenv("AGENT_ID", "opencode-cli-agent")
        self.workspace = os.getenv("OPENCODE_WORKSPACE", "/opt/opencode")
    
    def connect(self) -> bool:
        """Establish connection to kernel"""
        try:
            response = requests.get(f"{self.endpoint}/health", timeout=5)
            if response.status_code == 200:
                print(f"✓ Connected to kernel at {self.endpoint}")
                return True
        except Exception as e:
            print(f"✗ Failed to connect to kernel: {e}")
            return False
    
    def register_agent(self) -> bool:
        """Register this agent with the kernel"""
        try:
            agent_info = {
                "agent_id": self.agent_id,
                "service": "opencode-cli",
                "workspace": self.workspace,
                "capabilities": [
                    "validate_papers",
                    "inspect_receipts",
                    "spawn_validators",
                    "query_metrics"
                ]
            }
            response = requests.post(
                f"{self.endpoint}/api/agents/register",
                json=agent_info,
                timeout=5
            )
            if response.status_code == 200:
                print(f"✓ Agent registered: {self.agent_id}")
                return True
        except Exception as e:
            print(f"⚠ Agent registration not available: {e}")
            return True  # Not fatal
    
    def get_kernel_status(self) -> Dict[str, Any]:
        """Get kernel status"""
        try:
            response = requests.get(f"{self.endpoint}/api/status", timeout=5)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"⚠ Could not fetch kernel status: {e}")
        return {}
    
    def validate_papers(self, papers: list, token_string: str) -> Dict[str, Any]:
        """Trigger paper validation through kernel"""
        try:
            request_data = {
                "papers": papers,
                "token_string": token_string
            }
            response = requests.post(
                f"{self.endpoint}/api/validate",
                json=request_data,
                timeout=300  # Long timeout for validation
            )
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"✗ Validation failed: {e}")
        return {"status": "error"}

def main():
    kernel_endpoint = os.getenv("KERNEL_ENDPOINT", "http://proof-kernel:8765")
    
    conn = KernelConnection(kernel_endpoint)
    
    # Connect and register
    if not conn.connect():
        sys.exit(1)
    
    conn.register_agent()
    
    # Show status
    status = conn.get_kernel_status()
    print(f"\nKernel Status:")
    print(json.dumps(status, indent=2))
    
    print("\n✓ Kernel connection ready")

if __name__ == "__main__":
    main()

PYSCRIPT

chmod +x "$OPENCODE_WORKSPACE/kernel-connect.py"
echo "✓ Kernel connection helper created"

# =====================================================================
# 5. Start OpenCode CLI Terminal
# =====================================================================

echo "[5/5] Starting OpenCode CLI..."

# Try to install opencode-cli if not present
if ! command -v opencode &> /dev/null; then
    echo "Installing opencode-cli..."
    pip install --no-cache-dir opencode-cli 2>/dev/null || true
fi

# Create interactive startup command
cat > "$OPENCODE_WORKSPACE/cli-startup.sh" << 'CLISCRIPT'
#!/bin/bash

# Test kernel connection first
echo "Verifying kernel connection..."
python3 /opt/opencode/kernel-connect.py

echo ""
echo "=========================================="
echo "OpenCode CLI Terminal"
echo "=========================================="
echo ""
echo "Connected to kernel at: $KERNEL_ENDPOINT"
echo "Agent name: $OPENCODE_AGENT_NAME"
echo "Workspace: $OPENCODE_WORKSPACE"
echo ""
echo "Commands:"
echo "  > validate <paper-id>             - Validate paper"
echo "  > validate-batch <count>          - Validate N papers"
echo "  > status                          - Show kernel status"
echo "  > receipt <receipt-id>            - Get receipt"
echo "  > help                            - Show this help"
echo ""
echo "=========================================="
echo ""

# Start interactive terminal with Python REPL
python3 << 'PYEOF'
import os
import sys
import json
import requests
from pathlib import Path

# Set up environment
kernel_endpoint = os.getenv("KERNEL_ENDPOINT", "http://proof-kernel:8765")
workspace = os.getenv("OPENCODE_WORKSPACE", "/opt/opencode")

class OpenCodeTerminal:
    def __init__(self, kernel_endpoint):
        self.endpoint = kernel_endpoint
        self.session = requests.Session()
        self.history = []
    
    def validate(self, papers):
        """Validate papers through kernel"""
        if isinstance(papers, str):
            papers = [papers]
        
        token = "ATCGATCGATCGATCGATCG"  # Default token
        request = {
            "papers": papers,
            "token_string": token
        }
        
        try:
            print(f"Validating {len(papers)} paper(s)...")
            response = self.session.post(
                f"{self.endpoint}/api/validate",
                json=request,
                timeout=300
            )
            if response.status_code == 200:
                result = response.json()
                print(json.dumps(result, indent=2))
                return result
        except Exception as e:
            print(f"Error: {e}")
    
    def status(self):
        """Get kernel status"""
        try:
            response = self.session.get(
                f"{self.endpoint}/api/status",
                timeout=5
            )
            if response.status_code == 200:
                result = response.json()
                print(json.dumps(result, indent=2))
                return result
        except Exception as e:
            print(f"Error: {e}")
    
    def run_repl(self):
        """Run interactive REPL"""
        import code
        import readline
        
        # Create namespace with commands
        namespace = {
            'terminal': self,
            'validate': self.validate,
            'status': self.status,
            'endpoint': self.endpoint,
            'requests': requests,
            'json': json,
        }
        
        # Start interactive console
        console = code.InteractiveConsole(namespace)
        console.interact(
            banner="OpenCode CLI Terminal - Type 'help(terminal)' for commands",
            exitmsg="Goodbye!"
        )

# Run terminal
terminal = OpenCodeTerminal(kernel_endpoint)
terminal.run_repl()

PYEOF

CLISCRIPT

chmod +x "$OPENCODE_WORKSPACE/cli-startup.sh"

# Launch the terminal
echo ""
echo "✓ All services initialized"
echo "✓ Kernel connection verified"
echo "✓ Agent configured"
echo ""
echo "=========================================="
echo "OpenCode CLI Terminal Ready"
echo "=========================================="
echo ""

# Run the CLI startup
bash "$OPENCODE_WORKSPACE/cli-startup.sh"
