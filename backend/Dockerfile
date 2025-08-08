FROM python:3.11-slim

# Install OS deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Env vars for AWS creds
ENV AWS_REGION=ap-south-1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
