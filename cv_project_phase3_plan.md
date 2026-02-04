# CV Project Phase 3: Deployment Integration

## 🎯 Goal
Take the optimized ONNX model from `03_optimization_onnx.ipynb` and deploy it using **FastAPI** and **Docker**.

## 🛠️ Tasks
1. **Create `src/app.py`**: A FastAPI application that loads the ONNX model and exposes a `/predict` endpoint.
   - Input: Image file (UploadFile).
   - Validation: Check file type.
   - Preprocessing: Resize/Normalize (same as training).
   - Inference: ONNX Runtime.
   - Response: JSON with Bounding Boxes.

2. **Create `Dockerfile`**: 
   - Base Image: `python:3.9-slim`.
   - Dependencies: `fastapi`, `uvicorn`, `onnxruntime`, `python-multipart`, `opencv-python-headless`.
   - Entrypoint: Start Uvicorn.

3. **Create `docker-compose.yaml`**:
   - Service `api`: The FastAPI app.
   - Service `prometheus`: For monitoring (prep for Module 6).

4. **Update README**: Add instructions on how to run the Docker container.

## 📝 Implementation Plan
I will create the files directly in `cv_mlops_project/`.
