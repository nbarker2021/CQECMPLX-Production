FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy library code
COPY src/ /app/src/
COPY scripts/ /app/scripts/

# Create library directories
RUN mkdir -p /app/library/{documents,rag_cards,atomic_forms,morphonic_forms}

# Set environment variables
ENV PYTHONPATH=/app
ENV LIBRARY_PATH=/app/library
ENV PORT=8902

# Expose port
EXPOSE 8902

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8902/health')" || exit 1

# Run server
CMD ["python", "/app/src/library_server.py", "--serve"]
