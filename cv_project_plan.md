# 🏗️ Project Plan: End-to-End MLOps for Object Detection

## 🎯 Objective
Build a production-grade **Object Detection System** (e.g., detecting defects in manufacturing or potholes on roads) implementing MLOps best practices from Modules 1-4. This project will serve as the "spine" that connects all the individual lessons.

## 🛠️ Tech Stack
- **Task**: Object Detection (YOLOv8 or FasterRCNN)
- **Data**: Public Dataset (e.g., COCO-128 or specific subset)
- **Versioning**: DVC (Data) + Git (Code)
- **Tracking**: MLflow + Weights & Biases
- **Orchestration**: Prefect
- **Config**: Hydra
- **Optimization**: ONNX + Quantization

## 📅 Architecture Overview

### Phase 1: Setup & Data Engineering (Applying Modules 1, 2, 3)
1. **Repo Setup**: Cookiecutter structure, Poetry, Pre-commit.
2. **Data Pipeline**: 
   - Download raw images/labels.
   - Version raw data with DVC.
   - **ETL Job**: Resize/Normalize images, validate formats (Parquet metadata + JPG images).
   - **Feature Store**: Not strictly needed for images, but we will simulate metadata storage.

### Phase 2: Model Development (Applying Modules 2, 4, 4b)
1. **Experimentation**: Train YOLOv8n (Nano) basics.
2. **Tracking**: Log mAP, Precision, Recall to W&B.
3. **Hyperparameter Tuning**: Use Optuna to tune learning rate and augmentation.
4. **Optimization**: 
   - Pruning (make it smaller).
   - Quantization (FP32 -> INT8).
   - Export to ONNX.

### Phase 3: Future Integration (Deployment - Module 5)
- Dockerize the ONNX model.
- Serve via FastAPI.

---

## 📂 Proposed Folder Structure
```
cv_project/
  ├── conf/                 <- Hydra configs
  ├── data/                 <- DVC tracked
  ├── notebooks/            <- Exploration
  ├── src/
  │   ├── data/             <- ETL scripts
  │   ├── models/           <- Training logic (YOLO)
  │   └── visualization/    <- Inspection tools
  ├── tests/                <- PyTests
  ├── dvc.yaml              <- DVC Pipeline
  ├── pyproject.toml        <- Poetry deps
  └── README.md
```

## 📝 Next Steps
1. Create the project directory `cv_project`.
2. Initialize it with the standard structure (Cookiecutter manual simulation).
3. Create the pervasive `README.md` for this project.
4. Create **Notebook 1: Data Setup & Versioning** (DVC + Images).
5. Create **Notebook 2: Training & Tracking** (YOLO + W&B).
6. Create **Notebook 3: Optimization** (ONNX + Quantization).
