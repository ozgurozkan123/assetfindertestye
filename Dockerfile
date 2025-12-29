FROM python:3.11-slim

# Install system dependencies and Go toolchain to build assetfinder
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    build-essential \
    golang \
    && rm -rf /var/lib/apt/lists/*

# Install assetfinder (Go-based) and make sure GOPATH bin is on PATH
ENV GOPATH=/root/go
ENV PATH="$GOPATH/bin:$PATH"
RUN go install github.com/tomnomnom/assetfinder@latest

WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Render/Railway set PORT automatically
ENV HOST=0.0.0.0
EXPOSE 8000

CMD ["python", "server.py"]
