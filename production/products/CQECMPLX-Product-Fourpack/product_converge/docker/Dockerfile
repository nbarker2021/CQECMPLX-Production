# Converge — Production Docker Image
# Multi-stage build for minimal production image

# --- Build stage ---
FROM python:3.11-slim AS builder

WORKDIR /build
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# --- Production stage ---
FROM python:3.11-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy application code
COPY src/ ./src/
COPY proto/ ./proto/

# Set Python path
ENV PYTHONPATH=/app/src:$PYTHONPATH

# Expose ports
EXPOSE 8080 50051

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/health')" || exit 1

# Run the REST API server (default)
CMD ["python", "-m", "uvicorn", "api.rest_server:app", "--host", "0.0.0.0", "--port", "8080"]
