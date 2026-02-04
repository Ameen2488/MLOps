# Docker Commands Cheatsheet

Essential Docker commands for MLOps workflows.

---

## 🐳 Basic Docker Commands

### Images

```bash
# List images
docker images
docker image ls

# Pull an image
docker pull python:3.9-slim

# Build an image
docker build -t my-ml-app:v1 .
docker build -t my-ml-app:v1 -f Dockerfile.custom .

# Remove an image
docker rmi image-name:tag
docker rmi image-id

# Remove unused images
docker image prune
docker image prune -a  # Remove all unused images
```

---

### Containers

```bash
# Run a container
docker run image-name
docker run -d image-name                    # Detached mode
docker run -p 8000:8000 image-name         # Port mapping
docker run -v $(pwd):/app image-name       # Volume mount
docker run --name my-container image-name   # Named container
docker run -e ENV_VAR=value image-name     # Environment variables

# List containers
docker ps              # Running containers
docker ps -a           # All containers

# Stop a container
docker stop container-name
docker stop container-id

# Start a stopped container
docker start container-name

# Restart a container
docker restart container-name

# Remove a container
docker rm container-name
docker rm -f container-name  # Force remove running container

# Remove all stopped containers
docker container prune
```

---

### Logs & Debugging

```bash
# View logs
docker logs container-name
docker logs -f container-name              # Follow logs
docker logs --tail 100 container-name      # Last 100 lines

# Execute command in running container
docker exec container-name command
docker exec -it container-name /bin/bash   # Interactive shell

# Inspect container
docker inspect container-name

# View container stats
docker stats
docker stats container-name
```

---

## 🚀 ML/MLOps Specific Examples

### Example 1: Run Jupyter in Container

```bash
# Run Jupyter Lab
docker run -p 8888:8888 \
  -v $(pwd):/workspace \
  -e JUPYTER_ENABLE_LAB=yes \
  jupyter/scipy-notebook

# Custom ML image with Jupyter
docker run -p 8888:8888 \
  -v $(pwd):/app \
  -w /app \
  python:3.9 \
  bash -c "pip install jupyter && jupyter notebook --ip=0.0.0.0 --allow-root"
```

---

### Example 2: FastAPI ML Application

```bash
# Build
docker build -t ml-api:v1 .

# Run
docker run -d \
  -p 8000:8000 \
  --name ml-api \
  -e MODEL_PATH=/app/models/model.pkl \
  ml-api:v1

# Check logs
docker logs -f ml-api

# Test API
curl http://localhost:8000/health
```

---

### Example 3: MLflow Server

```bash
# Run MLflow tracking server
docker run -p 5000:5000 \
  -v $(pwd)/mlruns:/mlruns \
  ghcr.io/mlflow/mlflow:latest \
  mlflow server --host 0.0.0.0 --port 5000
```

---

## 🔧 Docker Compose

### Basic Commands

```bash
# Start services
docker-compose up
docker-compose up -d              # Detached
docker-compose up --build         # Rebuild images

# Stop services
docker-compose down
docker-compose down -v            # Remove volumes too

# View logs
docker-compose logs
docker-compose logs -f service-name

# List services
docker-compose ps

# Execute command in service
docker-compose exec service-name command
docker-compose exec api bash
```

---

### Example docker-compose.yml

```yaml
version: '3.8'

services:
  ml-api:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./models:/app/models
    environment:
      - MODEL_PATH=/app/models/model.pkl
    depends_on:
      - mlflow
  
  mlflow:
    image: ghcr.io/mlflow/mlflow:latest
    ports:
      - "5000:5000"
    volumes:
      - ./mlruns:/mlruns
    command: mlflow server --host 0.0.0.0 --port 5000
```

---

## 📦 Common Dockerfile Patterns

### Python ML Application

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY src/ ./src/
COPY models/ ./models/

# Expose port
EXPOSE 8000

# Run application
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

### Multi-stage Build (Smaller Image)

```dockerfile
# Build stage
FROM python:3.9 as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.9-slim

WORKDIR /app

# Copy dependencies from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy application
COPY src/ ./src/
COPY models/ ./models/

EXPOSE 8000
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 🧹 Cleanup Commands

```bash
# Remove all stopped containers
docker container prune

# Remove all unused images
docker image prune -a

# Remove all unused volumes
docker volume prune

# Remove all unused networks
docker network prune

# Remove everything (USE WITH CAUTION!)
docker system prune -a --volumes
```

---

## 💡 Best Practices

### 1. Use .dockerignore
```
__pycache__/
*.pyc
*.pyo
*.pyd
.git/
.pytest_cache/
.venv/
*.egg-info/
.env
.DS_Store
```

### 2. Multi-stage Builds
- Smaller final images
- Separate build dependencies from runtime

### 3. Layer Caching
- Order Dockerfile commands from least to most frequently changing
- Copy requirements.txt before code

### 4. Security
```bash
# Scan for vulnerabilities
docker scan image-name

# Run as non-root user
USER appuser
```

### 5. Tags
```bash
# Use specific versions, not 'latest'
FROM python:3.9.13-slim  # Good
FROM python:latest       # Bad
```

---

## 🔍 Troubleshooting

### Container won't start
```bash
# Check logs
docker logs container-name

# Check if port is in use
netstat -an | grep 8000  # Linux/Mac
netstat -an | findstr 8000  # Windows
```

### Out of disk space
```bash
# Check Docker disk usage
docker system df

# Clean up
docker system prune -a
```

### Permission issues with volumes
```bash
# Run with user ID
docker run -u $(id -u):$(id -g) ...
```

---

## 📚 Quick Reference Card

| Task | Command |
|------|---------|
| Build image | `docker build -t name:tag .` |
| Run container | `docker run -d -p 8000:8000 name:tag` |
| View logs | `docker logs -f container-name` |
| Stop container | `docker stop container-name` |
| Remove container | `docker rm container-name` |
| List running | `docker ps` |
| List all | `docker ps -a` |
| Shell into container | `docker exec -it container-name bash` |
| Clean up | `docker system prune -a` |

---

**Pro Tip**: Create aliases for common commands!

```bash
# Add to ~/.bashrc or ~/.zshrc
alias dps='docker ps'
alias dpa='docker ps -a'
alias di='docker images'
alias dlog='docker logs -f'
alias dex='docker exec -it'
```
