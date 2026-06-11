#!/bin/bash
# ============================================================================
# CQECMPLX Kernel - Ubuntu/WSL Native Installation
# ============================================================================
# Native Ubuntu installation for Linux and Windows WSL
# 
# This script:
#   - Installs all system dependencies natively
#   - Configures Python environment
#   - Sets up Docker (native or WSL)
#   - Installs and configures the kernel
#   - Launches all services
#
# Supported:
#   - Native Linux (Ubuntu 20.04+)
#   - Windows WSL2 (Ubuntu distribution)
#   - macOS (limited support)
#
# Usage:
#   sudo bash install-native.sh              # Full installation
#   sudo bash install-native.sh --dev-only   # Dev environment only
#   bash run-kernel.sh                       # Run after installation
#
# ============================================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
MAGENTA='\033[0;35m'
NC='\033[0m'

# Configuration
KERNEL_HOME="${HOME}/.local/cqecmplx-kernel"
VENV_PATH="${KERNEL_HOME}/venv"
KERNEL_REPO="D:\CQECMPLX-ProofValidatedSuite\kernel"
WSL_MOUNT="/mnt/d/CQECMPLX-ProofValidatedSuite/kernel"
INSTALL_LOG="/tmp/cqecmplx-install-${RANDOM}.log"

# =====================================================================
# Helper Functions
# =====================================================================

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1" | tee -a "$INSTALL_LOG"
}

log_success() {
    echo -e "${GREEN}[✓]${NC} $1" | tee -a "$INSTALL_LOG"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1" | tee -a "$INSTALL_LOG"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1" | tee -a "$INSTALL_LOG"
    exit 1
}

detect_environment() {
    log_info "Detecting environment..."
    
    if grep -qi "microsoft\|wsl" /proc/version 2>/dev/null; then
        echo "WSL2"
        export IS_WSL=true
    elif [ "$(uname)" = "Darwin" ]; then
        echo "MACOS"
        export IS_MACOS=true
    else
        echo "LINUX"
        export IS_LINUX=true
    fi
}

detect_wsl_home() {
    if [ "$IS_WSL" = true ]; then
        # Find Windows home directory mounted in WSL
        if [ -d "/mnt/c/Users/$USER" ]; then
            WSL_MOUNT="/mnt/c/Users/$USER/CQECMPLX-ProofValidatedSuite/kernel"
        elif [ -d "/mnt/d/CQECMPLX-ProofValidatedSuite" ]; then
            WSL_MOUNT="/mnt/d/CQECMPLX-ProofValidatedSuite/kernel"
        fi
        log_info "WSL mount detected: $WSL_MOUNT"
    fi
}

check_sudo() {
    if [ "$EUID" -ne 0 ] && [ "$1" != "--dev-only" ]; then
        log_error "This script requires sudo for system package installation. Run: sudo bash install-native.sh"
    fi
}

install_system_deps_ubuntu() {
    log_info "Installing system dependencies (Ubuntu)..."
    
    # Update package manager
    apt-get update -qq
    
    # Core dependencies
    apt-get install -y \
        build-essential \
        curl \
        git \
        wget \
        software-properties-common \
        apt-transport-https \
        ca-certificates \
        gnupg \
        lsb-release \
        2>&1 | tee -a "$INSTALL_LOG"
    
    log_success "System dependencies installed"
}

install_system_deps_macos() {
    log_info "Installing system dependencies (macOS)..."
    
    # Check if Homebrew is installed
    if ! command -v brew &> /dev/null; then
        log_info "Installing Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    
    # Install dependencies
    brew install -q \
        python@3.10 \
        git \
        curl \
        wget \
        2>&1 | tee -a "$INSTALL_LOG"
    
    log_success "System dependencies installed"
}

install_docker() {
    log_info "Installing Docker..."
    
    if command -v docker &> /dev/null; then
        log_success "Docker already installed: $(docker --version)"
        return 0
    fi
    
    if [ "$IS_WSL" = true ]; then
        log_info "WSL detected: Using Docker Desktop (install from Windows)"
        return 0
    fi
    
    if [ "$IS_MACOS" = true ]; then
        log_info "macOS detected: Using Docker Desktop (install from Homebrew or official)"
        return 0
    fi
    
    # Linux: Install Docker CE
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg 2>/dev/null
    
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
    
    apt-get update -qq
    apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin 2>&1 | tee -a "$INSTALL_LOG"
    
    # Start Docker
    systemctl start docker
    systemctl enable docker
    
    log_success "Docker installed and started"
}

add_docker_user() {
    if [ "$IS_WSL" = true ] || [ "$IS_MACOS" = true ]; then
        return 0
    fi
    
    log_info "Adding user to docker group..."
    
    if ! getent group docker > /dev/null; then
        groupadd docker
    fi
    
    usermod -aG docker "$SUDO_USER" 2>/dev/null || true
    
    log_success "Docker user group configured"
}

install_python_deps() {
    log_info "Installing Python dependencies..."
    
    # Ensure pip is up to date
    python3 -m pip install --upgrade pip setuptools wheel 2>&1 | tee -a "$INSTALL_LOG"
    
    # Install required packages
    python3 -m pip install --no-cache-dir \
        docker \
        docker-compose \
        requests \
        pydantic \
        cryptography \
        2>&1 | tee -a "$INSTALL_LOG"
    
    log_success "Python dependencies installed"
}

create_venv() {
    log_info "Creating Python virtual environment..."
    
    mkdir -p "$KERNEL_HOME"
    python3 -m venv "$VENV_PATH"
    
    # Activate venv
    # shellcheck source=/dev/null
    source "$VENV_PATH/bin/activate"
    
    # Upgrade pip
    pip install --upgrade pip setuptools wheel 2>&1 | tee -a "$INSTALL_LOG"
    
    log_success "Virtual environment created at $VENV_PATH"
}

create_native_launcher() {
    log_info "Creating native launcher script..."
    
    mkdir -p "$KERNEL_HOME/bin"
    
    cat > "$KERNEL_HOME/bin/kernel" << 'LAUNCHER'
#!/bin/bash
# Native CQECMPLX Kernel Launcher

KERNEL_HOME="${HOME}/.local/cqecmplx-kernel"
VENV_PATH="${KERNEL_HOME}/venv"
KERNEL_REPO="${KERNEL_HOME}/repo"

# Activate venv
source "${VENV_PATH}/bin/activate"

# Parse command
case "$1" in
    start|run)
        echo "Starting CQECMPLX Kernel..."
        cd "$KERNEL_REPO" || exit 1
        docker-compose -f docker-compose-kernel-with-opencode.yml up -d
        ;;
    stop|down)
        echo "Stopping CQECMPLX Kernel..."
        cd "$KERNEL_REPO" || exit 1
        docker-compose -f docker-compose-kernel-with-opencode.yml down
        ;;
    terminal|cli)
        echo "Accessing OpenCode CLI Terminal..."
        docker exec -it cqecmplx-opencode-cli python3 /opt/opencode/cli-startup.sh
        ;;
    logs)
        echo "Tailing kernel logs..."
        docker logs -f cqecmplx-proof-kernel
        ;;
    status)
        docker ps | grep cqecmplx
        ;;
    validate)
        shift
        docker exec -i cqecmplx-opencode-cli python3 << EOF
import requests, json
papers = ${2:-'["CQE-paper-00"]'}
if isinstance(papers, str):
    papers = [papers]
result = requests.post("http://proof-kernel:8765/api/validate", 
    json={"papers": papers, "token_string": "ATCGATCG"}).json()
print(json.dumps(result, indent=2))
EOF
        ;;
    *)
        echo "Usage: kernel {start|stop|terminal|logs|status|validate [papers]}"
        ;;
esac

LAUNCHER
    
    chmod +x "$KERNEL_HOME/bin/kernel"
    log_success "Launcher created at $KERNEL_HOME/bin/kernel"
}

setup_shell_integration() {
    log_info "Setting up shell integration..."
    
    local shell_rc="${HOME}/.bashrc"
    local init_line="export PATH=\"\$HOME/.local/cqecmplx-kernel/bin:\$PATH\""
    
    if [ ! -f "$shell_rc" ]; then
        touch "$shell_rc"
    fi
    
    if ! grep -q "cqecmplx-kernel" "$shell_rc"; then
        echo "" >> "$shell_rc"
        echo "# CQECMPLX Kernel" >> "$shell_rc"
        echo "$init_line" >> "$shell_rc"
    fi
    
    # Also for zsh if it exists
    if [ -f "${HOME}/.zshrc" ]; then
        if ! grep -q "cqecmplx-kernel" "${HOME}/.zshrc"; then
            echo "" >> "${HOME}/.zshrc"
            echo "# CQECMPLX Kernel" >> "${HOME}/.zshrc"
            echo "$init_line" >> "${HOME}/.zshrc"
        fi
    fi
    
    log_success "Shell integration complete"
}

copy_kernel_files() {
    log_info "Copying kernel files to native location..."
    
    mkdir -p "$KERNEL_HOME/repo"
    
    if [ -d "$WSL_MOUNT" ]; then
        cp -r "$WSL_MOUNT"/* "$KERNEL_HOME/repo/" 2>/dev/null || true
        log_success "Files copied from WSL mount"
    elif [ -d "$KERNEL_REPO" ]; then
        cp -r "$KERNEL_REPO"/* "$KERNEL_HOME/repo/" 2>/dev/null || true
        log_success "Files copied from Windows"
    else
        log_warn "Kernel repo not found, continuing without files"
    fi
}

show_setup_summary() {
    clear
    
    echo -e "${MAGENTA}"
    cat << 'BANNER'
╔══════════════════════════════════════════════════════════════╗
║   CQECMPLX Kernel - Native Installation Complete            ║
╚══════════════════════════════════════════════════════════════╝
BANNER
    echo -e "${NC}"
    
    echo -e "${GREEN}Installation Summary:${NC}"
    echo "  • Environment: $(detect_environment)"
    echo "  • Home: $KERNEL_HOME"
    echo "  • Virtual Env: $VENV_PATH"
    echo "  • Kernel Repo: $KERNEL_HOME/repo"
    echo ""
    
    echo -e "${GREEN}Quick Commands:${NC}"
    echo "  • Start kernel:      ${BLUE}kernel start${NC}"
    echo "  • Stop kernel:       ${BLUE}kernel stop${NC}"
    echo "  • Terminal:          ${BLUE}kernel terminal${NC}"
    echo "  • Validate papers:   ${BLUE}kernel validate${NC}"
    echo "  • View logs:         ${BLUE}kernel logs${NC}"
    echo "  • Check status:      ${BLUE}kernel status${NC}"
    echo ""
    
    if [ "$IS_WSL" = true ]; then
        echo -e "${YELLOW}WSL Integration:${NC}"
        echo "  • Windows files mounted at: /mnt/d or /mnt/c"
        echo "  • Shared Docker daemon: ✓"
        echo "  • File sync: Automatic"
        echo ""
    fi
    
    echo -e "${GREEN}Next Steps:${NC}"
    echo "  1. Start a new terminal or run: source ~/.bashrc"
    echo "  2. Start kernel:   kernel start"
    echo "  3. Access terminal: kernel terminal"
    echo "  4. Validate papers: kernel validate"
    echo ""
    
    echo -e "${GREEN}Installation Log:${NC}"
    echo "  $INSTALL_LOG"
    echo ""
}

# =====================================================================
# Main Installation
# =====================================================================

main() {
    echo -e "${MAGENTA}"
    cat << 'BANNER'
╔══════════════════════════════════════════════════════════════╗
║   CQECMPLX Kernel - Ubuntu/WSL Native Installation          ║
╚══════════════════════════════════════════════════════════════╝
BANNER
    echo -e "${NC}"
    
    log_info "Installation started at $(date)"
    
    # Detection
    ENVIRONMENT=$(detect_environment)
    log_info "Detected environment: $ENVIRONMENT"
    
    if [ "$ENVIRONMENT" = "WSL2" ]; then
        export IS_WSL=true
        detect_wsl_home
    elif [ "$ENVIRONMENT" = "MACOS" ]; then
        export IS_MACOS=true
    else
        export IS_LINUX=true
    fi
    
    # Checks
    check_sudo "$1"
    log_info "Pre-flight checks passed"
    
    # Installation phases
    if [ "$1" != "--dev-only" ]; then
        if [ "$IS_MACOS" = true ]; then
            install_system_deps_macos
        elif [ "$ENVIRONMENT" != "WSL2" ]; then
            install_system_deps_ubuntu
        fi
        
        install_docker
        [ "$ENVIRONMENT" != "WSL2" ] && [ "$ENVIRONMENT" != "MACOS" ] && add_docker_user
    fi
    
    install_python_deps
    create_venv
    copy_kernel_files
    create_native_launcher
    setup_shell_integration
    
    log_success "Installation completed at $(date)"
    show_setup_summary
}

# =====================================================================
# Entry Point
# =====================================================================

case "${1:-}" in
    --help)
        cat << 'EOF'
Usage: sudo bash install-native.sh [options]

Options:
  (no option)    Full installation with Docker
  --dev-only     Install Python environment only (no Docker)
  --help         Show this help

This script installs CQECMPLX Kernel natively on:
  - Native Linux (Ubuntu 20.04+)
  - Windows WSL2 (Ubuntu)
  - macOS

After installation, use: kernel start

EOF
        ;;
    *)
        main "$@"
        ;;
esac
