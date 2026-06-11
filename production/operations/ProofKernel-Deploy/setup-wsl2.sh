#!/bin/bash
# ============================================================================
# CQECMPLX Kernel - WSL2 Configuration
# ============================================================================
# Optimizes WSL2 for CQECMPLX Kernel development
#
# Run on Ubuntu WSL2 distribution to:
#   - Configure Docker daemon
#   - Set resource limits
#   - Enable file sharing with Windows
#   - Optimize WSL integration
#
# Usage:
#   bash setup-wsl2.sh
#
# ============================================================================

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
MAGENTA='\033[0;35m'
NC='\033[0m'

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[✓]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

configure_wsl_config() {
    log_info "Configuring WSL resource limits..."
    
    # Create .wslconfig in Windows home
    if [ -d "/mnt/c/Users/$USER" ]; then
        CONFIG_FILE="/mnt/c/Users/$USER/.wslconfig"
    else
        log_warn "Could not find Windows home directory"
        return 1
    fi
    
    cat > "$CONFIG_FILE" << 'EOF'
[wsl2]
# Memory allocation (8GB)
memory=8GB

# CPU allocation (4 cores)
processors=4

# Swap size (2GB)
swap=2GB

# Virtual disk size (limit to 512GB)
localhostForwarding=true

# Enable nested virtualization
nestedVirtualization=true

# vGPU support (optional, uncomment if using GPU)
# guiApplications=true

# Enable Hyper-V socket
# hypervSocketAddress=auto
EOF
    
    log_success "WSL config created at $CONFIG_FILE"
    log_warn "Please restart WSL for changes to take effect: wsl --shutdown"
}

configure_docker_wsl() {
    log_info "Configuring Docker for WSL..."
    
    # Ensure Docker service is running
    if ! command -v dockerd &> /dev/null; then
        log_warn "Docker not installed in WSL. Install via Windows Docker Desktop."
        return 1
    fi
    
    # Configure Docker daemon
    mkdir -p /etc/docker
    
    cat > /etc/docker/daemon.json << 'EOF'
{
  "storage-driver": "overlay2",
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m",
    "max-file": "10"
  },
  "live-restore": true,
  "userland-proxy": false
}
EOF
    
    log_success "Docker daemon configured"
}

setup_shared_folders() {
    log_info "Setting up shared folders..."
    
    # Create symbolic links for easy access
    ln -sf /mnt/c/Users ~/"Windows Home" 2>/dev/null || true
    ln -sf /mnt/d /home/d 2>/dev/null || true
    
    log_success "Shared folders linked"
}

optimize_file_sync() {
    log_info "Optimizing file synchronization..."
    
    # Configure git for WSL to avoid CRLF issues
    git config --global core.autocrlf input
    git config --global core.fileMode true
    
    log_success "Git configured for WSL"
}

test_docker_integration() {
    log_info "Testing Docker integration..."
    
    if ! docker ps &>/dev/null; then
        log_warn "Docker not accessible. Ensure Docker Desktop is running on Windows."
        return 1
    fi
    
    log_success "Docker integration working"
}

show_wsl_summary() {
    clear
    
    echo -e "${MAGENTA}"
    cat << 'BANNER'
╔══════════════════════════════════════════════════════════════╗
║   WSL2 Configuration Complete                               ║
╚══════════════════════════════════════════════════════════════╝
BANNER
    echo -e "${NC}"
    
    echo -e "${GREEN}Configuration Summary:${NC}"
    echo "  • Memory: 8GB"
    echo "  • CPU Cores: 4"
    echo "  • Swap: 2GB"
    echo "  • Storage Driver: overlay2"
    echo "  • Docker Daemon: Configured"
    echo ""
    
    echo -e "${GREEN}WSL Integration:${NC}"
    echo "  • Windows mount: /mnt/c (C: drive)"
    echo "  • Other mounts: /mnt/d, /mnt/e, etc."
    echo "  • Home link: ~/Windows Home"
    echo "  • Docker: Shared with Windows"
    echo ""
    
    echo -e "${YELLOW}Important:${NC}"
    echo "  1. Restart WSL for .wslconfig changes:"
    echo "     ${BLUE}wsl --shutdown${NC}"
    echo ""
    echo "  2. Verify Docker is running:"
    echo "     ${BLUE}docker ps${NC}"
    echo ""
    echo "  3. Then install kernel natively:"
    echo "     ${BLUE}sudo bash install-native.sh${NC}"
    echo ""
}

main() {
    echo -e "${MAGENTA}"
    cat << 'BANNER'
╔══════════════════════════════════════════════════════════════╗
║   CQECMPLX Kernel - WSL2 Configuration                       ║
╚══════════════════════════════════════════════════════════════╝
BANNER
    echo -e "${NC}"
    
    log_info "Configuring WSL2 environment..."
    echo ""
    
    configure_wsl_config
    configure_docker_wsl
    setup_shared_folders
    optimize_file_sync
    test_docker_integration
    
    echo ""
    show_wsl_summary
}

main "$@"
