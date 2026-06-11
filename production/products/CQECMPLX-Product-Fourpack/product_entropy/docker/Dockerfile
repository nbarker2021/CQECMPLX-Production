# EntropyCore API Server — Docker Image
# =====================================
# Build:
#   docker build -f docker/Dockerfile -t entropycore:latest .
# Run:
#   docker run -p 8000:8000 entropycore:latest

FROM python:3.12-slim AS builder

WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY docker/requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# ─────────────────────────────────────────────────────────────────────────────

FROM python:3.12-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY src/core/ /app/src/core/
COPY src/api/ /app/src/api/

# Set Python path
ENV PYTHONPATH=/app/src:$PYTHONPATH
ENV PATH=/root/.local/bin:$PATH

# Expose API port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# Run server
CMD ["python", "-m", "uvicorn", "api.server:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
