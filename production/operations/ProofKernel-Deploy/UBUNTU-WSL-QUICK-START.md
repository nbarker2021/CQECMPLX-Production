# 🚀 UBUNTU/WSL NATIVE — QUICK START

## Install (One Command)

### Linux or WSL2 Ubuntu

```bash
cd D:\CQECMPLX-ProofValidatedSuite\kernel
sudo bash install-native.sh
```

**That's it.** Installation takes ~5 minutes.

---

## After Installation

### Reload Shell
```bash
source ~/.bashrc
```

### Start Kernel
```bash
kernel start
```

### Access Terminal
```bash
kernel terminal
```

### Validate Papers
```bash
kernel validate
```

---

## Commands

```bash
kernel start           # Start all services
kernel stop            # Stop all services  
kernel terminal        # Open interactive CLI
kernel validate        # Validate papers
kernel logs            # View kernel logs
kernel status          # Show running services
```

---

## Locations

```
Kernel Home:    ~/.local/cqecmplx-kernel
Virtual Env:    ~/.local/cqecmplx-kernel/venv
Repo:           ~/.local/cqecmplx-kernel/repo
Launcher:       ~/.local/cqecmplx-kernel/bin/kernel
```

---

## WSL2 Specific

### First Time Only

```bash
# Optimize WSL2
bash setup-wsl2.sh

# Restart WSL
wsl --shutdown

# Reinstall kernel
sudo bash install-native.sh
```

### File Access

```bash
# Windows C: drive
/mnt/c/Users/Username/...

# Windows D: drive
/mnt/d/CQECMPLX-ProofValidatedSuite/...

# Symlink
~/Windows\ Home
```

### Docker

Docker automatically shares between Windows and WSL. Just ensure Docker Desktop is running on Windows.

---

## Verify Installation

```bash
# Check command
which kernel

# Check venv
ls ~/.local/cqecmplx-kernel/venv

# Check Docker
docker ps

# Start kernel
kernel start

# Verify services
kernel status
```

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Command not found | `source ~/.bashrc` |
| Docker not running | Start Docker Desktop |
| Permission denied | Run with `sudo` |
| Files not found | Copy from `/mnt/d/...` |

---

## Workflow

```bash
# 1. Install once
sudo bash install-native.sh

# 2. Every session
kernel start
kernel terminal
> validate(["CQE-paper-00"])

# 3. Done
kernel stop
```

---

**Native installation complete!** 🐧

Run `kernel start` and you're ready to go.
