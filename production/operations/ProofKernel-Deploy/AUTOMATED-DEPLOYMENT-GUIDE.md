# 🚀 AUTOMATED DEPLOYMENT GUIDE

## One-Command Deployment

Everything is now automated into a single deployment script that launches all containers and services.

---

## 🎯 Quick Start (Choose Your Platform)

### On Linux/macOS

```bash
cd D:\CQECMPLX-ProofValidatedSuite\kernel

# Basic deployment
bash deploy-kernel.sh

# Deploy + validate papers
bash deploy-kernel.sh --full-validate

# Deploy + watch logs
bash deploy-kernel.sh --logs

# Stop all services
bash deploy-kernel.sh --stop

# Get help
bash deploy-kernel.sh --help
```

### On Windows (PowerShell)

```powershell
cd D:\CQECMPLX-ProofValidatedSuite\kernel

# Basic deployment
.\deploy-kernel.ps1

# Deploy + validate papers
.\deploy-kernel.ps1 -FullValidate

# Deploy + watch logs
.\deploy-kernel.ps1 -Logs

# Stop all services
.\deploy-kernel.ps1 -Stop

# Get help
.\deploy-kernel.ps1 -Help
```

---

## 🔄 What The Script Does

### Phase 1: Pre-Flight Checks
- ✅ Verifies Docker is installed and running
- ✅ Verifies Docker Compose is installed
- ✅ Checks compose file exists
- ✅ Creates necessary directories

### Phase 2: Setup
- ✅ Stops any existing services
- ✅ Creates startup scripts
- ✅ Ensures images are available

### Phase 3: Deployment
- ✅ Starts all Docker services
- ✅ Verifies services are running
- ✅ Waits for kernel to be ready
- ✅ Checks health endpoints

### Phase 4: Reporting
- ✅ Shows service status dashboard
- ✅ Displays API endpoints
- ✅ Lists quick commands
- ✅ Optionally validates papers or watches logs

---

## 📊 Deployment Output

When deployment completes, you'll see:

```
╔══════════════════════════════════════════════════════════════╗
║   CQECMPLX Hierarchical Kernel - Deployment Complete         ║
╚══════════════════════════════════════════════════════════════╝

✓ Services Running:
  • cqecmplx-proof-kernel
  • cqecmplx-opencode-cli
  • cqecmplx-docker-provider

✓ Kernel Status:
  Kernel responding

Quick Commands:
  # Access OpenCode terminal:
    docker exec -it cqecmplx-opencode-cli python3 /opt/opencode/cli-startup.sh

  # Run validation:
    docker exec -i cqecmplx-opencode-cli python3 << 'EOF'
    import requests
    requests.post('http://proof-kernel:8765/api/validate',
        json={'papers': ['CQE-paper-00'], 'token_string': 'ATCGATCG'}).json()
    EOF

  # Monitor hierarchy:
    watch 'docker ps -a | grep paper-validator'

  # View logs:
    docker logs -f cqecmplx-proof-kernel
    docker logs -f cqecmplx-opencode-cli

API Endpoints:
  • Proof Kernel:   http://localhost:8765
  • OpenCode CLI:   http://localhost:8766
```

---

## 🎮 Command Reference

### Bash (Linux/macOS)

```bash
# Deploy all services
bash deploy-kernel.sh

# Deploy + validate papers (takes 5-10 min)
bash deploy-kernel.sh --full-validate

# Deploy + watch logs in real-time
bash deploy-kernel.sh --logs

# Stop and remove all containers
bash deploy-kernel.sh --stop

# Get help
bash deploy-kernel.sh --help
```

### PowerShell (Windows)

```powershell
# Deploy all services
.\deploy-kernel.ps1

# Deploy + validate papers (takes 5-10 min)
.\deploy-kernel.ps1 -FullValidate

# Deploy + watch logs in real-time
.\deploy-kernel.ps1 -Logs

# Stop and remove all containers
.\deploy-kernel.ps1 -Stop

# Get help
.\deploy-kernel.ps1 -Help
```

---

## 📈 Advanced Usage

### Monitor Deployment in Real-Time

Open multiple terminals:

```bash
# Terminal 1: Deployment
bash deploy-kernel.sh

# Terminal 2: Watch services
watch 'docker ps -a | grep cqecmplx'

# Terminal 3: Watch hierarchy
watch 'docker ps -a | grep paper-validator'

# Terminal 4: Monitor resources
watch 'docker stats --no-stream'
```

### Run Full Validation (All 32 Papers)

```bash
# Deploy + validate automatically
bash deploy-kernel.sh --full-validate

# Or manually after deployment
docker exec -i cqecmplx-opencode-cli python3 << 'EOF'
import requests, json

result = requests.post("http://proof-kernel:8765/api/validate", json={
    "papers": [f"CQE-paper-{i:02d}" for i in range(32)],
    "token_string": "ATCGATCGATCGATCGATCG"
}).json()

print(f"Validated: {result['papers_validated']}")
print(f"Passed: {result['papers_passed']}")
print(f"Failed: {result['papers_failed']}")
EOF
```

### Interactive Terminal Access

```bash
# After deployment
docker exec -it cqecmplx-opencode-cli python3 /opt/opencode/cli-startup.sh

# Inside the terminal:
> validate("CQE-paper-00")
> validate(["CQE-paper-00", "CQE-paper-01"])
> status()
```

---

## 🔍 Troubleshooting

### Services won't start
```bash
# Check logs
docker logs cqecmplx-proof-kernel
docker logs cqecmplx-opencode-cli

# Manually stop and try again
bash deploy-kernel.sh --stop
bash deploy-kernel.sh
```

### Kernel not responding
```bash
# Wait a bit longer (sometimes takes 30-60 seconds)
sleep 60

# Check health manually
docker exec cqecmplx-proof-kernel curl http://localhost:8765/health
```

### Docker daemon not running
```bash
# Linux
sudo systemctl start docker

# macOS
open /Applications/Docker.app

# Windows
# Open Docker Desktop from Start menu
```

### Permission denied on scripts
```bash
# Linux/macOS
chmod +x deploy-kernel.sh

# Windows PowerShell (as Administrator)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 📊 File Structure

```
kernel/
├── deploy-kernel.sh           (14.4 KB) ← Bash deployment
├── deploy-kernel.ps1          (11.1 KB) ← PowerShell deployment
├── docker-compose-kernel-with-opencode.yml
├── scripts/
│   └── opencode-start.sh      (Auto-created)
└── data/
    └── (Auto-created)
```

---

## ✅ Verification

After deployment completes, verify everything is working:

```bash
# 1. Check all services running
docker ps | grep cqecmplx
# Expected: 3 services (kernel, opencode, provider)

# 2. Check kernel health
curl http://localhost:8765/health
# Expected: 200 OK

# 3. Check OpenCode CLI responds
docker exec cqecmplx-opencode-cli curl http://proof-kernel:8765/health
# Expected: 200 OK

# 4. Validate a paper
docker exec -i cqecmplx-opencode-cli python3 << 'EOF'
import requests
r = requests.post("http://proof-kernel:8765/api/validate", 
    json={"papers": ["CQE-paper-00"], "token_string": "ATCGATCG"})
print(f"Status: {r.status_code}")
print(f"Result: {r.json()['results'][0]['status']}")
EOF
```

---

## 🎯 Typical Workflow

```bash
# 1. Deploy
bash deploy-kernel.sh
# Takes ~30-60 seconds

# 2. Wait for ready
# Script automatically waits for kernel

# 3. Access terminal
docker exec -it cqecmplx-opencode-cli python3 /opt/opencode/cli-startup.sh

# 4. Validate papers
> validate(["CQE-paper-00"])

# 5. Monitor spawning (in separate terminal)
watch 'docker ps -a | grep paper-validator'

# 6. When done, stop
bash deploy-kernel.sh --stop
```

---

## 📈 Performance Notes

### Deployment Time
- Basic deployment: ~30 seconds
- First validation of 1 paper: ~10 seconds
- Full suite (32 papers): ~5-10 minutes
- Docker image pulls (if needed): ~2-5 minutes

### Resource Usage
- Proof Kernel: 4GB RAM (steady)
- OpenCode CLI: 2GB RAM (steady)
- Level 1 validators: 2GB each (spawned on demand)
- Typical idle: ~6GB total

---

## 🔐 Security Notes

- Scripts run containers with restricted permissions
- Docker socket mounted read-only where possible
- No credentials in scripts
- Agents auto-register with kernel
- All communication on Docker network

---

## 🎉 You're Ready!

Everything is now automated. Just run:

```bash
# Linux/macOS
bash deploy-kernel.sh

# Windows
.\deploy-kernel.ps1
```

And your entire hierarchical kernel with OpenCode CLI is running! 🚀

---

## 📞 Common Tasks After Deployment

### Start Interactive Terminal
```bash
docker exec -it cqecmplx-opencode-cli python3 /opt/opencode/cli-startup.sh
```

### Run Validation
```bash
docker exec -i cqecmplx-opencode-cli python3 << 'EOF'
import requests
requests.post("http://proof-kernel:8765/api/validate", 
    json={"papers": ["CQE-paper-00"], "token_string": "ATCGATCG"})
EOF
```

### View Logs
```bash
docker logs -f cqecmplx-proof-kernel
docker logs -f cqecmplx-opencode-cli
```

### Stop Everything
```bash
bash deploy-kernel.sh --stop  # or .\deploy-kernel.ps1 -Stop
```

---

**Deployment Complete! Your kernel is ready for production.** 🎉
