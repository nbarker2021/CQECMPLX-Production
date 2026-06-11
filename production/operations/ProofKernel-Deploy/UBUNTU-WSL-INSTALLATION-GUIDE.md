# 🐧 UBUNTU/WSL NATIVE INSTALLATION GUIDE

## Overview

Your CQECMPLX Kernel now runs **natively on Ubuntu/WSL** with seamless Windows integration.

```
Windows PowerShell/CMD
    ↓
WSL2 Ubuntu (native Linux kernel)
    ↓
CQECMPLX Kernel (runs natively)
    ↓
Docker Desktop (shared with Windows)
    ↓
Python/Validation Services
```

---

## 🚀 Quick Install

### On Linux (Native)

```bash
# 1. Download installation script
cd /tmp
wget https://your-repo/install-native.sh
# Or copy the file manually

# 2. Run installation
sudo bash install-native.sh

# 3. Reload shell
source ~/.bashrc

# 4. Start kernel
kernel start
```

### On Windows (WSL2)

```bash
# 1. Open WSL2 Ubuntu terminal
wsl

# 2. Run installation
sudo bash ~/CQECMPLX-ProofValidatedSuite/kernel/install-native.sh

# 3. Reload shell
source ~/.bashrc

# 4. Start kernel
kernel start
```

---

## 📋 What Gets Installed

### System Dependencies (Ubuntu)
- `build-essential` — C/C++ compiler
- `python3` — Python interpreter
- `docker-ce` — Docker engine
- `git`, `curl`, `wget` — Standard tools

### Python Environment
- Virtual environment at `~/.local/cqecmplx-kernel/venv`
- Docker Python SDK
- Docker Compose
- All kernel dependencies

### Native Launcher
- Command-line tool: `kernel`
- Located at: `~/.local/cqecmplx-kernel/bin/kernel`
- Added to PATH automatically

### Kernel Files
- Copied from Windows to: `~/.local/cqecmplx-kernel/repo`
- Accessible from both Windows and Linux

---

## 🎮 Usage

### Start Kernel
```bash
kernel start
```
Launches all services (proof-kernel, opencode-cli, docker-provider)

### Stop Kernel
```bash
kernel stop
```
Gracefully shuts down all services

### Access Terminal
```bash
kernel terminal
```
Opens interactive OpenCode CLI REPL

### Validate Papers
```bash
kernel validate
```
Validates papers through OpenCode terminal

### View Logs
```bash
kernel logs
```
Streams kernel logs in real-time

### Check Status
```bash
kernel status
```
Shows running containers

---

## 🔧 WSL2 Configuration

If using WSL2, run the optimization script first:

```bash
bash setup-wsl2.sh
```

This configures:
- Memory allocation (8GB)
- CPU cores (4)
- Docker integration
- File sharing
- Resource limits

**Then restart WSL:**
```bash
wsl --shutdown
```

---

## 📁 Installation Paths

```
~/.local/cqecmplx-kernel/
├── bin/
│   └── kernel              ← Command-line launcher
├── venv/                   ← Python virtual environment
│   ├── bin/
│   ├── lib/
│   └── pyvenv.cfg
└── repo/                   ← Kernel repository
    ├── docker-compose-kernel-with-opencode.yml
    ├── scripts/
    ├── cmplx_proof_kernel/
    └── ...
```

---

## 🔗 WSL Integration

### Accessing Windows Files

From Ubuntu WSL, Windows drives are mounted:
```bash
# C: drive
/mnt/c/Users/YourUsername/...

# D: drive  
/mnt/d/CQECMPLX-ProofValidatedSuite/...

# Symlink for convenience
~/Windows\ Home  → /mnt/c/Users/YourUsername
```

### Docker Shared Daemon

Docker runs natively on both:
- **Windows**: Docker Desktop
- **WSL2**: Uses Docker Desktop's daemon
- **Automatic**: No additional setup needed

### File Synchronization

Files are automatically synced:
```bash
# Edit on Windows
C:\Users\YourUsername\work\file.py

# Access from Ubuntu
~/Windows\ Home/work/file.py

# Or mounted directly
/mnt/c/Users/YourUsername/work/file.py
```

---

## ✅ Verification

After installation, verify everything works:

```bash
# 1. Check kernel command exists
which kernel
# Expected: ~/.local/cqecmplx-kernel/bin/kernel

# 2. Check venv
ls ~/.local/cqecmplx-kernel/venv
# Expected: bin, lib, pyvenv.cfg

# 3. Check Docker
docker ps
# Expected: No error, shows containers

# 4. Start kernel
kernel start
# Expected: Services start without error

# 5. Verify services
kernel status
# Expected: Shows 3 running containers

# 6. Test validation
kernel validate
# Expected: Python execution succeeds
```

---

## 🎯 Workflow Example

### On Windows
```powershell
# Edit files in Windows
code C:\CQECMPLX-ProofValidatedSuite\kernel

# View in Explorer
explorer D:\CQECMPLX-ProofValidatedSuite
```

### On WSL2 Ubuntu
```bash
# Open Ubuntu terminal
wsl

# Start kernel
kernel start

# Access terminal
kernel terminal

# Validate papers
> validate("CQE-paper-00")

# View files
ls ~/.local/cqecmplx-kernel/repo

# Edit with Linux tools
vim ~/.local/cqecmplx-kernel/repo/deploy-kernel.sh
```

### Synchronized
- Changes on Windows appear instantly in WSL
- Changes in WSL appear instantly on Windows
- Docker can access both

---

## 🐛 Troubleshooting

### "Command not found: kernel"
```bash
# Reload shell
source ~/.bashrc

# Or check path
echo $PATH | grep cqecmplx-kernel

# Or run directly
~/.local/cqecmplx-kernel/bin/kernel start
```

### "Docker daemon not running"
**On Windows:**
- Start Docker Desktop
- Wait for Docker icon to show as ready

**On WSL:**
```bash
# WSL shares Docker with Windows
# Ensure Docker Desktop is running on Windows
docker ps
```

### "Permission denied" on install
```bash
# Must use sudo for system packages
sudo bash install-native.sh

# Or use --dev-only to skip Docker
bash install-native.sh --dev-only
```

### "No such file or directory" for repo
- Installation copies files from Windows automatically
- If files not copied, manually copy:
```bash
cp -r /mnt/d/CQECMPLX-ProofValidatedSuite/kernel/* ~/.local/cqecmplx-kernel/repo/
```

---

## 🚀 Advanced Usage

### Custom Virtual Environment Location
```bash
# Edit install-native.sh
VENV_PATH="/custom/path/venv"

# Then reinstall
sudo bash install-native.sh
```

### Using Native Package Manager Versions
```bash
# Instead of Docker, use native Python
~/.local/cqecmplx-kernel/venv/bin/python -m cmplx_proof_kernel.orchestrator
```

### Integration with IDE

**VS Code (WSL Remote)**
```
1. Install "Remote - WSL" extension
2. Open folder in WSL: /home/user/.local/cqecmplx-kernel/repo
3. Terminal opens in WSL automatically
4. Run: kernel start
```

**JetBrains IDE**
```
1. Settings → Project → Python Interpreter
2. Select: ~/.local/cqecmplx-kernel/venv/bin/python
3. Terminal shows WSL environment
```

**Sublime/vim**
```bash
# Edit from command line
code ~/.local/cqecmplx-kernel/repo/Dockerfile
vim ~/.local/cqecmplx-kernel/repo/deploy-kernel.sh
```

---

## 📊 System Requirements

### Minimum
- 4GB RAM
- 2 CPU cores
- 20GB disk space
- Ubuntu 20.04+ (or WSL2)

### Recommended
- 8GB RAM
- 4 CPU cores
- 50GB disk space
- Ubuntu 22.04+ (or WSL2 with latest Ubuntu)

---

## 🔐 Security

### Permissions
- Kernel runs as regular user (not root)
- Docker requires group membership (added automatically)
- Python venv is user-isolated

### Network
- Services bind to localhost (127.0.0.1)
- Not accessible from network
- WSL internal only

### File Access
- Windows files shared read-write
- Docker can access both filesystems
- No special permissions needed

---

## 📈 Performance

### Native Linux
- Full performance
- Direct hardware access
- Best for production

### WSL2
- Near-native performance
- ~5-10% overhead vs native
- Excellent for development

### Docker
- Container-level isolation
- Resource limits respected
- Efficient memory usage

---

## 🎉 What You Can Now Do

✅ Run kernel natively on Linux
✅ Run kernel natively on Windows (WSL2)
✅ Edit files on Windows, validate on Linux
✅ Use same Docker daemon
✅ Share files seamlessly
✅ Integrated terminal access
✅ Production-ready setup

---

## 🚀 Getting Started

```bash
# 1. Install
sudo bash install-native.sh

# 2. Reload shell
source ~/.bashrc

# 3. Start kernel
kernel start

# 4. Validate
kernel validate

# 5. Access terminal
kernel terminal

# Done! 🎉
```

---

## 📝 Uninstall

To remove native installation:

```bash
# Stop kernel
kernel stop

# Remove home directory
rm -rf ~/.local/cqecmplx-kernel

# Remove shell integration
# Edit ~/.bashrc and remove CQECMPLX lines
nano ~/.bashrc
```

---

**Native Ubuntu/WSL installation complete and ready for production!** 🐧
