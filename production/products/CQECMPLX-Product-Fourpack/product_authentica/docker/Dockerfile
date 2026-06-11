# Authentica — Production Dockerfile
# =====================================
# Multi-stage build for optimal image size.
# 
# Build:
#   docker build -f docker/Dockerfile -t authentica:latest .
# Run:
#   docker run -p 8000:8000 -e AUTHENTICA_SECRET=<set-secret> authentica:latest
# Or use docker-compose (recommended):
#   docker-compose up -d

# ── Stage 1: Builder ──
FROM python:3.12-slim AS builder

WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# ── Stage 2: Production ──
FROM python:3.12-slim AS production

LABEL maintainer="Authentica Engineering <engineering@authentica.io>"
LABEL description="Authentica — Anti-counterfeit authentication platform"
LABEL version="1.0.0"

WORKDIR /app

# Create non-root user for security
RUN groupadd -r authentica && useradd -r -g authentica authentica

# Copy installed packages from builder
COPY --from=builder /root/.local /home/authentica/.local
ENV PATH=/home/authentica/.local/bin:$PATH

# Copy application code
COPY src/ ./src/
COPY requirements.txt .

# Set proper ownership
RUN chown -R authentica:authentica /app /home/authentica

# Switch to non-root user
USER authentica

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# Environment defaults
ENV AUTHENTICA_ENV=production
ENV AUTHENTICA_RATE_LIMIT=1000
ENV PYTHONPATH=/app/src
ENV PYTHONUNBUFFERED=1

# Run the API server
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
