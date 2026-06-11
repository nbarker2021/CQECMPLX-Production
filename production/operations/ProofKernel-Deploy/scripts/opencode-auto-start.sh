#!/bin/bash
# ============================================================================
# OpenCode CLI Auto-Start with Pre-Auth in Docker
# ============================================================================
# This runs INSIDE the opencode-terminal container
# Auto-starts on container launch, waits for user to auth
#
# ============================================================================

set -e

# =====================================================================
# Configuration
# =====================================================================

KERNEL_ENDPOINT="${KERNEL_ENDPOINT:-http://proof-kernel:8765}"
OPENCODE_WORKSPACE="${OPENCODE_WORKSPACE:-/opt/opencode}"
OPENCODE_DATA_PATH="${OPENCODE_DATA_PATH:-/home/developer/.opencode}"
AGENT_NAME="${OPENCODE_AGENT_NAME:-cqecmplx-agent}"

# =====================================================================
# Setup Phase
# =====================================================================

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║   OpenCode CLI - Initializing (Container Mode)                ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Create directories
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
    ],
    "security": {
      "require_auth": false,
      "audit_logging": true
    }
  }
}
EOF

echo "✓ Agent configuration created"

# =====================================================================
# Kernel Connection Test
# =====================================================================

echo ""
echo "Testing kernel connection..."

python3 << 'PYEOF'
import os
import sys
import json
import requests
import time

kernel_endpoint = os.getenv("KERNEL_ENDPOINT", "http://proof-kernel:8765")

for attempt in range(1, 6):
    try:
        response = requests.get(f"{kernel_endpoint}/health", timeout=5)
        if response.status_code == 200:
            print(f"✓ Connected to kernel at {kernel_endpoint}")
            break
    except Exception as e:
        if attempt < 5:
            print(f"  Attempt {attempt}/5: Waiting for kernel...")
            time.sleep(2)
        else:
            print(f"✗ Could not connect to kernel after 5 attempts")
            print(f"  Make sure proof-kernel is running")

PYEOF

echo ""

# =====================================================================
# OpenCode Terminal - Ready for Auth
# =====================================================================

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║   OpenCode CLI Terminal - Ready for Login                     ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "Available commands:"
echo "  • validate()           - Validate papers"
echo "  • validate([papers])   - Validate specific papers"
echo "  • status()             - Get kernel status"
echo "  • requests             - HTTP client"
echo "  • terminal             - Terminal object"
echo ""
echo "────────────────────────────────────────────────────────────────"
echo ""

# =====================================================================
# Interactive Python Shell with Kernel Integration
# =====================================================================

python3 << 'TERMINAL_SHELL'
import os
import sys
import json
import code
import requests
import readline

kernel_endpoint = os.getenv("KERNEL_ENDPOINT", "http://proof-kernel:8765")
workspace = os.getenv("OPENCODE_WORKSPACE", "/opt/opencode")

class OpenCodeTerminal:
    """OpenCode CLI Terminal with Kernel Integration"""
    
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.session = requests.Session()
        self.session.timeout = 300
    
    def validate(self, papers=None, token=None):
        """
        Validate papers through the kernel.
        
        Usage:
          validate()                          # Default: CQE-paper-00
          validate("CQE-paper-00")            # Single paper
          validate(["CQE-paper-00", ...])     # Multiple papers
          validate(["CQE-paper-00"], "ATCG...")  # With token
        """
        if papers is None:
            papers = ["CQE-paper-00"]
        elif isinstance(papers, str):
            papers = [papers]
        
        if token is None:
            token = "ATCGATCGATCGATCGATCG"
        
        try:
            print(f"[OpenCode] Validating {len(papers)} paper(s)...")
            print(f"[OpenCode] Endpoint: {self.endpoint}/api/validate")
            
            response = self.session.post(
                f"{self.endpoint}/api/validate",
                json={
                    "papers": papers,
                    "token_string": token
                },
                timeout=300
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"[OpenCode] ✓ Validation complete")
                print(f"[OpenCode] Papers: {result.get('papers_validated', 0)}")
                print(f"[OpenCode] Passed: {result.get('papers_passed', 0)}")
                print(f"[OpenCode] Failed: {result.get('papers_failed', 0)}")
                print("")
                print(json.dumps(result, indent=2))
                return result
            else:
                print(f"[OpenCode] ✗ Error: {response.status_code}")
                print(response.text)
        
        except Exception as e:
            print(f"[OpenCode] ✗ Error: {e}")
    
    def status(self):
        """Get kernel status."""
        try:
            print(f"[OpenCode] Fetching kernel status...")
            response = self.session.get(f"{self.endpoint}/api/status", timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                print(f"[OpenCode] ✓ Kernel status:")
                print("")
                print(json.dumps(result, indent=2))
                return result
        except Exception as e:
            print(f"[OpenCode] ✗ Error: {e}")
    
    def health(self):
        """Check kernel health."""
        try:
            response = self.session.get(f"{self.endpoint}/health", timeout=5)
            print(f"[OpenCode] Kernel: {'✓ Healthy' if response.status_code == 200 else '✗ Unhealthy'}")
            return response.status_code == 200
        except Exception as e:
            print(f"[OpenCode] ✗ Kernel unreachable: {e}")
            return False
    
    def help(self):
        """Show help."""
        print("""
[OpenCode] Available Commands:
  
  validate()                    # Validate CQE-paper-00
  validate("CQE-paper-00")      # Validate specific paper
  validate([...])               # Validate multiple papers
  status()                      # Get kernel status
  health()                      # Check kernel health
  help()                        # Show this help
  
[OpenCode] Available Objects:
  
  terminal                      # Terminal instance
  requests                      # HTTP client
  json                          # JSON utilities
  endpoint                      # Kernel endpoint URL
  
[OpenCode] Examples:

  # Single paper
  validate("CQE-paper-00")
  
  # Multiple papers
  validate(["CQE-paper-00", "CQE-paper-01", "CQE-paper-02"])
  
  # Check status
  status()
  
  # Direct HTTP request
  requests.get(endpoint + "/health")
""")

# Initialize terminal
terminal = OpenCodeTerminal(kernel_endpoint)

# Show initial status
print("[OpenCode] Checking kernel health...")
terminal.health()
print("")

# Create interactive namespace
namespace = {
    'terminal': terminal,
    'validate': terminal.validate,
    'status': terminal.status,
    'health': terminal.health,
    'help': terminal.help,
    'requests': requests,
    'json': json,
    'endpoint': kernel_endpoint,
}

# Start interactive console
print("[OpenCode] Starting interactive terminal...\n")
console = code.InteractiveConsole(namespace)

# Custom banner
banner = """
╔════════════════════════════════════════════════════════════════╗
║   OpenCode CLI Terminal - Logged In                           ║
║                                                                ║
║   Kernel connected: http://proof-kernel:8765                 ║
║   Type 'help()' for available commands                        ║
╚════════════════════════════════════════════════════════════════╝

"""

console.interact(banner=banner, exitmsg="[OpenCode] Goodbye!")

TERMINAL_SHELL
