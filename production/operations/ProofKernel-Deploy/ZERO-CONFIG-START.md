# 🚀 ONE-COMMAND START - EVERYTHING AUTO-CONFIGURED

## Just Run It

```bash
bash start.sh
```

or on Windows:

```batch
start.bat
```

That's it. Your kernel starts, OpenCode CLI boots up, and waits for you to log in and start typing.

---

## ⚡ What Happens

1. **Containers Start** (~30 seconds)
   - Proof Kernel launches (Level 0)
   - OpenCode CLI launches (Level 1)
   - Docker provider starts

2. **OpenCode Terminal Boots** (~10 seconds)
   - Agent auto-configures
   - Kernel connection established
   - Terminal waits for you

3. **Ready for Input** (Immediate)
   - Just type your command
   - No setup needed
   - All functions available

---

## 📝 Immediate Usage

After running `start.sh` or `start.bat`, you see:

```
╔════════════════════════════════════════════════════════════════╗
║   OpenCode CLI Terminal is Running                            ║
╚════════════════════════════════════════════════════════════════╝

OpenCode terminal is waiting for you to connect.

Access it with:

  docker exec -it cqecmplx-opencode-cli bash

Then in the terminal, just start typing:
  > validate("CQE-paper-00")
  > validate(["CQE-paper-00", "CQE-paper-01"])
  > status()

All commands are ready to go!
```

---

## 🔌 Access The Terminal

```bash
docker exec -it cqecmplx-opencode-cli bash
```

You're now in the OpenCode CLI terminal. Just type:

```python
> validate("CQE-paper-00")
Validating 1 paper(s)...
[OpenCode] ✓ Validation complete
Papers: 1
Passed: 1
Failed: 0

{
  "orchestrator_id": "orch-xyz",
  "papers_validated": 1,
  ...
}

>
```

---

## 💬 Available Commands

Just type in the terminal:

```python
# Validate single paper
validate("CQE-paper-00")

# Validate multiple papers
validate(["CQE-paper-00", "CQE-paper-01"])

# Check status
status()

# Check health
health()

# Get help
help()

# Direct HTTP
requests.get(endpoint + "/health")
```

---

## 🎯 Example Workflow

```bash
# Terminal 1: Start everything
bash start.sh

# Wait for message saying terminal is ready

# Terminal 2: Access terminal
docker exec -it cqecmplx-opencode-cli bash

# Now you're in OpenCode CLI, just type:
> validate("CQE-paper-00")
> validate(["CQE-paper-00", "CQE-paper-01", "CQE-paper-02"])
> status()
```

---

## 🔍 What's Running

```bash
# See all services
docker ps | grep cqecmplx
```

You'll see:
```
cqecmplx-proof-kernel      Running (4GB, 4 CPU)
cqecmplx-opencode-cli      Running (2GB, 2 CPU)
cqecmplx-docker-provider   Running
```

---

## 📊 Monitor in Separate Terminal

```bash
# Watch hierarchy spawn
watch 'docker ps -a | grep paper-validator'

# View kernel logs
docker logs -f cqecmplx-proof-kernel

# View OpenCode logs
docker logs -f cqecmplx-opencode-cli

# Check resources
docker stats
```

---

## 🛑 Stop Everything

```bash
# Stop all services
docker-compose -f docker-compose-kernel-with-opencode.yml down

# Or just close the terminal
# Services will auto-clean on exit
```

---

## ✨ Key Features

✅ **One command to launch**
✅ **Auto-configured OpenCode CLI**
✅ **Pre-authenticated (no login needed)**
✅ **All functions available immediately**
✅ **Just type your commands**
✅ **Results print to terminal**
✅ **Kernel integrated**
✅ **Paper validators spawn on demand**

---

## 🎉 That's It!

```bash
bash start.sh
docker exec -it cqecmplx-opencode-cli bash
> validate("CQE-paper-00")
```

No setup, no configuration, no waiting. Just **run, connect, type**. 

Your entire infrastructure is ready to go! 🚀

---

## 📁 File Summary

- **start.sh** (Linux/macOS) — Launch script
- **start.bat** (Windows) — Launch script
- **opencode-auto-start.sh** — Auto-boot script (runs in container)
- **docker-compose-kernel-with-opencode.yml** — Services definition

---

## 🚀 Quick Reference

| Task | Command |
|------|---------|
| Start all | `bash start.sh` |
| Access terminal | `docker exec -it cqecmplx-opencode-cli bash` |
| Validate | `> validate(...)` |
| Status | `> status()` |
| Logs | `docker logs -f cqecmplx-proof-kernel` |
| Stop | `docker-compose down` |

---

**One command. One terminal. Infinite validation.** 🎯

Everything is already set up and waiting for your input!
