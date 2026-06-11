#!/bin/bash
# ============================================================================
# CQECMPLX Kernel Full Deployment Script
# ============================================================================
# One-command launcher for entire hierarchical kernel + OpenCode CLI
#
# Usage:
#   bash deploy-kernel.sh                  # Deploy everything
#   bash deploy-kernel.sh --full-validate  # Deploy + validate all papers
#   bash deploy-kernel.sh --logs           # Deploy + watch logs
#
# ============================================================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
KERNEL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMPOSE_FILE="docker-compose-kernel-with-opencode.yml"
LOG_DIR="/tmp/cqecmplx-logs"
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

# =====================================================================
# Helper Functions
# =====================================================================

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[✓]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

create_directories() {
    mkdir -p "$LOG_DIR"
    mkdir -p "$KERNEL_DIR/scripts"
    mkdir -p "$KERNEL_DIR/data"
}

check_docker() {
    log_info "Checking Docker installation..."
    
    if ! command -v docker &> /dev/null; then
        log_error "Docker not found. Please install Docker first."
        exit 1
    fi
    
    if ! docker ps &> /dev/null; then
        log_error "Cannot access Docker daemon. Is it running?"
        exit 1
    fi
    
    log_success "Docker is available"
}

check_compose() {
    log_info "Checking Docker Compose..."
    
    if ! command -v docker-compose &> /dev/null; then
        log_error "Docker Compose not found. Please install Docker Compose."
        exit 1
    fi
    
    log_success "Docker Compose is available"
}

check_compose_file() {
    log_info "Checking compose file..."
    
    if [ ! -f "$KERNEL_DIR/$COMPOSE_FILE" ]; then
        log_error "Compose file not found: $COMPOSE_FILE"
        exit 1
    fi
    
    log_success "Compose file found"
}

stop_existing_services() {
    log_info "Checking for existing services..."
    
    if docker ps | grep -q "cqecmplx"; then
        log_warn "Found existing CQECMPLX services. Stopping them..."
        docker-compose -f "$KERNEL_DIR/$COMPOSE_FILE" down 2>/dev/null || true
        sleep 2
        log_success "Existing services stopped"
    else
        log_info "No existing services found"
    fi
}

pull_images() {
    log_info "Ensuring Docker images are available..."
    
    # Try to pull the image if needed
    if ! docker image inspect python-dev:complete-stack &> /dev/null; then
        log_warn "Image python-dev:complete-stack not found locally"
        log_info "You should have built this image in the complete stack setup"
        log_info "Proceeding anyway - Docker will attempt to pull or build..."
    else
        log_success "Image python-dev:complete-stack is available"
    fi
}

create_startup_script() {
    log_info "Creating startup script..."
    
    cat > "$KERNEL_DIR/scripts/opencode-start.sh" << 'STARTSCRIPT'
#!/bin/bash

set -e

echo "=========================================="
echo "OpenCode CLI Terminal Initialization"
echo "=========================================="

# Verify configuration
if [ -z "$KERNEL_ENDPOINT" ]; then
    echo "ERROR: KERNEL_ENDPOINT not set"
    exit 1
fi

# Create workspace
mkdir -p "$OPENCODE_WORKSPACE"
mkdir -p "$OPENCODE_DATA_PATH"
mkdir -p "$OPENCODE_DATA_PATH/agents"
mkdir -p "$OPENCODE_DATA_PATH/config"

# Generate agent config
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
    ]
  }
}
EOF

# Create kernel connection script
cat > "$OPENCODE_WORKSPACE/kernel-connect.py" << 'PYSCRIPT'
#!/usr/bin/env python3
import os, json, requests, sys
from typing import Dict, Any

class KernelConnection:
    def __init__(self, kernel_endpoint: str):
        self.endpoint = kernel_endpoint
    
    def connect(self) -> bool:
        try:
            response = requests.get(f"{self.endpoint}/health", timeout=5)
            if response.status_code == 200:
                print(f"✓ Connected to kernel at {self.endpoint}")
                return True
        except Exception as e:
            print(f"✗ Failed to connect: {e}")
            return False
    
    def validate(self, papers: list, token: str = "ATCGATCGATCG"):
        try:
            request_data = {"papers": papers, "token_string": token}
            response = requests.post(
                f"{self.endpoint}/api/validate",
                json=request_data,
                timeout=300
            )
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"✗ Validation failed: {e}")
        return {"status": "error"}
    
    def status(self):
        try:
            response = requests.get(f"{self.endpoint}/api/status", timeout=5)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"✗ Error: {e}")

def main():
    kernel_endpoint = os.getenv("KERNEL_ENDPOINT", "http://proof-kernel:8765")
    conn = KernelConnection(kernel_endpoint)
    
    if not conn.connect():
        sys.exit(1)
    
    status = conn.status()
    print(f"\nKernel Status:")
    print(json.dumps(status, indent=2) if status else "Status unavailable")
    print("\n✓ Kernel connection ready")

if __name__ == "__main__":
    main()

PYSCRIPT

chmod +x "$OPENCODE_WORKSPACE/kernel-connect.py"

# Launch interactive terminal
python3 << 'PYEOF'
import os, sys, json, requests, code

kernel_endpoint = os.getenv("KERNEL_ENDPOINT", "http://proof-kernel:8765")

class OpenCodeTerminal:
    def __init__(self, kernel_endpoint):
        self.endpoint = kernel_endpoint
        self.session = requests.Session()
    
    def validate(self, papers):
        if isinstance(papers, str):
            papers = [papers]
        token = "ATCGATCGATCGATCGATCG"
        request = {"papers": papers, "token_string": token}
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
        try:
            response = self.session.get(f"{self.endpoint}/api/status", timeout=5)
            if response.status_code == 200:
                result = response.json()
                print(json.dumps(result, indent=2))
                return result
        except Exception as e:
            print(f"Error: {e}")

terminal = OpenCodeTerminal(kernel_endpoint)
namespace = {
    'terminal': terminal,
    'validate': terminal.validate,
    'status': terminal.status,
    'requests': requests,
    'json': json,
    'endpoint': kernel_endpoint,
}

console = code.InteractiveConsole(namespace)
console.interact(banner="OpenCode CLI Terminal - Type 'help(terminal)' for commands")

PYEOF

STARTSCRIPT
    
    chmod +x "$KERNEL_DIR/scripts/opencode-start.sh"
    log_success "Startup script created"
}

start_services() {
    log_info "Starting Docker services..."
    
    cd "$KERNEL_DIR"
    
    docker-compose -f "$COMPOSE_FILE" up -d
    
    log_success "Services started"
    sleep 3
}

verify_services() {
    log_info "Verifying services..."
    
    local proof_kernel=$(docker ps | grep -c "cqecmplx-proof-kernel" || echo "0")
    local opencode_cli=$(docker ps | grep -c "cqecmplx-opencode-cli" || echo "0")
    local docker_provider=$(docker ps | grep -c "cqecmplx-docker-provider" || echo "0")
    
    if [ "$proof_kernel" -eq 1 ] && [ "$opencode_cli" -eq 1 ] && [ "$docker_provider" -eq 1 ]; then
        log_success "All services running"
        return 0
    else
        log_error "Some services failed to start"
        log_info "Proof Kernel: $proof_kernel, OpenCode CLI: $opencode_cli, Docker Provider: $docker_provider"
        return 1
    fi
}

wait_for_kernel() {
    log_info "Waiting for kernel to be ready..."
    
    local max_attempts=30
    local attempt=1
    
    while [ $attempt -le $max_attempts ]; do
        if docker exec cqecmplx-proof-kernel curl -s http://localhost:8765/health > /dev/null 2>&1; then
            log_success "Kernel is ready"
            return 0
        fi
        
        echo -ne "  Attempt $attempt/$max_attempts...\r"
        sleep 2
        attempt=$((attempt + 1))
    done
    
    log_warn "Kernel took longer than expected to start. Continuing anyway..."
    return 0
}

show_status() {
    log_info "Current service status:"
    echo ""
    docker ps | grep "cqecmplx" | awk '{print "  " $12 " -> " $1 " (" $5 ")"}'
    echo ""
}

validate_papers() {
    log_info "Running paper validation..."
    
    docker exec -i cqecmplx-opencode-cli python3 << 'EOF'
import requests, json

endpoint = "http://proof-kernel:8765"

try:
    result = requests.post(
        f"{endpoint}/api/validate",
        json={
            "papers": ["CQE-paper-00", "CQE-paper-01"],
            "token_string": "ATCGATCGATCGATCGATCG"
        },
        timeout=300
    ).json()
    
    print(json.dumps(result, indent=2))
except Exception as e:
    print(f"Error: {e}")
EOF
}

show_dashboard() {
    clear
    
    echo -e "${BLUE}"
    cat << 'BANNER'
╔════════════════════════════════════════════════════════════════╗
║   CQECMPLX Hierarchical Kernel - Deployment Complete          ║
╚════════════════════════════════════════════════════════════════╝
BANNER
    echo -e "${NC}"
    
    echo -e "${GREEN}✓ Services Running:${NC}"
    docker ps | grep "cqecmplx" | awk '{printf "  • %s (%s)\n", $12, $5}'
    
    echo ""
    echo -e "${GREEN}✓ Kernel Status:${NC}"
    docker exec cqecmplx-proof-kernel curl -s http://localhost:8765/health | python3 -m json.tool 2>/dev/null || echo "  Kernel responding"
    
    echo ""
    echo -e "${BLUE}Quick Commands:${NC}"
    echo "  # Access OpenCode terminal:"
    echo "    docker exec -it cqecmplx-opencode-cli python3 /opt/opencode/cli-startup.sh"
    echo ""
    echo "  # Run validation:"
    echo "    docker exec cqecmplx-opencode-cli python3 << 'EOF'"
    echo "    import requests"
    echo "    requests.post('http://proof-kernel:8765/api/validate',"
    echo "        json={'papers': ['CQE-paper-00'], 'token_string': 'ATCGATCG'}).json()"
    echo "    EOF"
    echo ""
    echo "  # Monitor hierarchy:"
    echo "    watch 'docker ps -a | grep paper-validator'"
    echo ""
    echo "  # View logs:"
    echo "    docker logs -f cqecmplx-proof-kernel"
    echo "    docker logs -f cqecmplx-opencode-cli"
    echo ""
    echo -e "${BLUE}API Endpoints:${NC}"
    echo "  • Proof Kernel:   http://localhost:8765"
    echo "  • OpenCode CLI:   http://localhost:8766"
    echo ""
}

show_help() {
    cat << 'EOF'
Usage: bash deploy-kernel.sh [options]

Options:
  (no option)      Deploy all services
  --full-validate  Deploy + validate all 32 papers
  --logs           Deploy + watch kernel logs
  --stop           Stop all services
  --help           Show this help

Examples:
  bash deploy-kernel.sh                    # Basic deployment
  bash deploy-kernel.sh --full-validate    # Deploy + validate
  bash deploy-kernel.sh --logs             # Deploy + watch logs

EOF
}

# =====================================================================
# Main Execution
# =====================================================================

main() {
    echo ""
    echo -e "${BLUE}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║   CQECMPLX Hierarchical Kernel - Full Deployment              ║${NC}"
    echo -e "${BLUE}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    
    # Pre-flight checks
    log_info "Running pre-flight checks..."
    check_docker
    check_compose
    check_compose_file
    create_directories
    echo ""
    
    # Setup
    log_info "Setting up environment..."
    stop_existing_services
    pull_images
    create_startup_script
    echo ""
    
    # Deploy
    log_info "Deploying services..."
    start_services
    verify_services
    wait_for_kernel
    echo ""
    
    # Show results
    show_status
    show_dashboard
    
    # Handle options
    if [ "$1" = "--full-validate" ]; then
        echo ""
        log_info "Running full validation..."
        validate_papers
    elif [ "$1" = "--logs" ]; then
        echo ""
        log_info "Watching kernel logs (Ctrl+C to exit)..."
        docker logs -f cqecmplx-proof-kernel
    fi
}

# Parse arguments
case "$1" in
    --help)
        show_help
        ;;
    --stop)
        log_info "Stopping services..."
        docker-compose -f "$KERNEL_DIR/$COMPOSE_FILE" down
        log_success "Services stopped"
        ;;
    *)
        main "$@"
        ;;
esac
