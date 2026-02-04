# CV MLOps Project: Object Detection 🚀

An end-to-end Computer Vision project demonstrating the **MLOps Principles** learned in the curriculum.

## 🏗️ Architecture
1. **Data**: COCO-128 (Small dataset for speed) managed by **DVC**.
2. **Model**: YOLOv8 (State-of-the-art Object Detection).
3. **Training**: Tracked with **Weights & Biases**.
4. **Config**: Managed by **Hydra**.
5. **Optimization**: Exported to **ONNX** via **Quantization**.

## 📂 Structure
- `conf/`: Configuration files (Hydra).
- `data/`: Raw and processed data (Git ignored, DVC tracked).
- `notebooks/`: Interactive lessons/experiments.
- `src/`: Production source code.
- `pyproject.toml`: Dependency management.

## 🚀 Getting Started

### 1. Install Dependencies
```bash
pip install poetry
poetry install
```

### 2. Follow the Notebooks
Start with `notebooks/01_data_setup.ipynb`.

### 3. Deployment (Phase 3)
Run the API locally using Docker:
```bash
# Build and Run
docker-compose up --build

# Test API
# Open http://localhost:8000/docs
```
