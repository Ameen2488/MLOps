# Dockerfile for CV MLOps Project
FROM python:3.9-slim

# Prevent python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY pyproject.toml .
# We convert poetry to pip requirements for simple docker build
# Or just install essentials manually for this demo to save time
RUN pip install fastapi uvicorn onnxruntime python-multipart opencv-python-headless pillow

# Copy Source Code
COPY src/ src/
# Copy Models (In prod, you normally pull from S3/DVC, but we copy local for now)
COPY notebooks/*.onnx notebooks/

# Expose Port
EXPOSE 8000

# Run
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
