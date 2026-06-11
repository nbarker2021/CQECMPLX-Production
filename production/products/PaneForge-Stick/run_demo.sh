#!/bin/sh
cd "$(dirname "$0")"
python3 kernel/paneforge_kernel.py 8770 &
sleep 2
xdg-open http://localhost:8770/ 2>/dev/null || open http://localhost:8770/
