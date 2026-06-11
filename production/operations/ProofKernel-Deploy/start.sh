#!/bin/bash
# ============================================================================
# CQECMPLX Kernel - One-Line Launch
# ============================================================================
# 
# Just run this script and your kernel starts with OpenCode CLI ready
# Everything is auto-configured, just log in and start typing
#
# Usage:
#   bash start.sh
#
# ============================================================================

cd "$(dirname "${BASH_SOURCE[0]}")" || exit 1

COMPOSE_FILE="docker-compose-kernel-with-opencode.yml"

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║   CQECMPLX Kernel - Launching                                  ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Check if services are already running
if docker ps 2>/dev/null | grep -q "cqecmplx-proof-kernel"; then
    echo "[INFO] Services already running"
    echo ""
    echo "Access OpenCode terminal:"
    echo "  docker exec -it cqecmplx-opencode-cli bash"
    echo ""
    exit 0
fi

# Start services
echo "[INFO] Starting services..."
docker-compose -f "$COMPOSE_FILE" up -d

# Wait for kernel
echo "[INFO] Waiting for kernel to be ready..."
for i in {1..30}; do
    if docker exec cqecmplx-proof-kernel curl -s http://localhost:8765/health >/dev/null 2>&1; then
        echo "[INFO] ✓ Kernel is ready"
        break
    fi
    echo -ne "  Attempt $i/30...\r"
    sleep 1
done

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║   OpenCode CLI Terminal is Running                            ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "OpenCode terminal is waiting for you to connect."
echo ""
echo "Access it with:"
echo ""
echo "  docker exec -it cqecmplx-opencode-cli bash"
echo ""
echo "Then in the terminal, just start typing:"
echo "  > validate(\"CQE-paper-00\")"
echo "  > validate([\"CQE-paper-00\", \"CQE-paper-01\"])"
echo "  > status()"
echo ""
echo "All commands are ready to go!"
echo ""
