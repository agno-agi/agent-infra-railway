# Test Railway Agent Dockerfile
FROM agnohq/python:3.12

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN uv pip install -r requirements.txt --system

# Copy application code
COPY infra/ ./infra/
COPY app.py .

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
  CMD curl -f http://localhost:${PORT:-8000}/health || exit 1

# Run AgentOS with dynamic port from Railway
CMD sh -c "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}"
