# 🗺️ MLOps Learning Program - Navigation Guide

**Quick reference to jump to any lesson, exercise, or project in the program.**

---

## 📌 Quick Start

- **Main Overview**: [README.md](./README.md)
- **Setup Guide**: [tools_and_setup/installation_guide.md](./tools_and_setup/installation_guide.md)
- **All Reference Links**: [resources/reference_links.md](./resources/reference_links.md)
- **Implementation Plan**: [Brain Folder - Implementation Plan](C:\Users\asidd\.gemini\antigravity\brain\5edcb4f6-06bf-48dc-b9c7-453d7b6b4f9b\implementation_plan.md)

---

## 🎯 Module 1: Foundations & Background

**Location**: `module_01_foundations/`  
**Duration**: 2 weeks  
**Status**: 🟢 Lesson 1 Complete | 🟡 In Progress

| Lesson | File | Topics | Status |
|--------|------|--------|--------|
| 1 | [lesson_01_intro_to_mlops.ipynb](./module_01_foundations/lesson_01_intro_to_mlops.ipynb) | MLOps intro, importance, maturity levels | ✅ Complete |
| 2 | [lesson_02_mlops_vs_devops.ipynb](./module_01_foundations/lesson_02_mlops_vs_devops.ipynb) | Differences, testing complexity | 🔄 Creating |
| 3 | [lesson_03_ml_lifecycle.ipynb](./module_01_foundations/lesson_03_ml_lifecycle.ipynb) | Data → Train → Deploy → Monitor | 🔄 Creating |

**Module README**: [module_01_foundations/README.md](./module_01_foundations/README.md)
**Exercises**: [ex01_foundations.md](./module_01_foundations/exercises/ex01_foundations.md)

---

## 🔁 Module 2: Reproducibility & Versioning

**Location**: `module_02_reproducibility/`  
**Duration**: 3 weeks  
**Topics**: DVC, MLflow, Weights & Biases  
**Status**: 🟡 In Progress

| # | Lesson | File | Key Topics | Interview Focus |
|---|--------|------|------------|-----------------|
| 1 | Why Reproducibility | [lesson_01_why_reproducibility.ipynb](./module_02_reproducibility/lesson_01_why_reproducibility.ipynb) | Determinism, debugging, compliance | "Why does reproducibility matter?" | 🔄 Creating |
| 2 | Git & DVC | [lesson_02_git_and_dvc.ipynb](./module_02_reproducibility/lesson_02_git_and_dvc.ipynb) | Data versioning, DVC pipelines | "How do you version large datasets?" | 🔄 Creating |
| 3 | MLflow Basics | [lesson_03_mlflow_basics.ipynb](./module_02_reproducibility/lesson_03_mlflow_basics.ipynb) | Tracking, experiments, UI | "How do you track experiments?" | 🔄 Creating |
| 4 | MLflow PyTorch | [lesson_04_mlflow_pytorch.ipynb](./module_02_reproducibility/lesson_04_mlflow_pytorch.ipynb) | Deep learning tracking | "Track training at scale" | 🔄 Creating |
| 5 | W&B Intro | [lesson_05_wandb_intro.ipynb](./module_02_reproducibility/lesson_05_wandb_intro.ipynb) | W&B features, setup | "MLflow vs W&B?" | 🔄 Creating |
| 6 | W&B + sklearn | [lesson_06_wandb_sklearn.ipynb](./module_02_reproducibility/lesson_06_wandb_sklearn.ipynb) | Complete ML workflow | "Production experiment tracking" | 🔄 Creating |
| 7 | W&B + PyTorch | [lesson_07_wandb_pytorch.ipynb](./module_02_reproducibility/lesson_07_wandb_pytorch.ipynb) | DL with W&B | "Real-time training viz" | 🔄 Creating |
| 8 | MLflow vs W&B | [lesson_08_mlflow_vs_wandb.ipynb](./module_02_reproducibility/lesson_08_mlflow_vs_wandb.ipynb) | Comparison, best practices | "Which tool for what use case?" | 🔄 Creating |

**Module README**: [module_02_reproducibility/README.md](./module_02_reproducibility/README.md) ✅

**Exercises**: [ex02_reproducibility.ipynb](./module_02_reproducibility/exercises/ex02_reproducibility.ipynb)

**Project**: [Reproducible Pipeline](./module_02_reproducibility/projects/reproducible_pipeline/)

---

## 🗄️ Module 3: Data & Pipeline Engineering

**Location**: `module_03_data_engineering/`  
**Duration**: 4 weeks  
**Topics**: ETL, Sampling, Leakage, Feast, Spark, Prefect  
**Status**: 🟡 In Progress

| # | Lesson | File | Key Topics | Interview Focus |
|---|--------|------|------------|-----------------|
| 1 | Data Sources & Formats | [lesson_01_data_sources_formats.ipynb](./module_03_data_engineering/lesson_01_data_sources_formats.ipynb) | CSV vs Parquet, compression | "Why Parquet over CSV?" | 🔄 Creating |
| 2 | ETL Pipelines | [lesson_02_etl_pipelines.ipynb](./module_03_data_engineering/lesson_02_etl_pipelines.ipynb) | ETL vs ELT, idempotency | "Design a data pipeline" | 🔄 Creating |
| 3 | Sampling Strategies | [lesson_03_sampling_strategies.ipynb](./module_03_data_engineering/lesson_03_sampling_strategies.ipynb) | SMOTE, imbalanced data | "Handle 0.1% fraud data" | 🔄 Creating |
| 4 | Data Leakage | [lesson_04_data_leakage.ipynb](./module_03_data_engineering/lesson_04_data_leakage.ipynb) | Detection, prevention | "99% accuracy fails in prod" | 🔄 Creating |
| 5 | Feature Stores (Feast) | [lesson_05_feature_stores_feast.ipynb](./module_03_data_engineering/lesson_05_feature_stores_feast.ipynb) | Point-in-time joins, versioning | "Training-serving skew?" | 🔄 Creating |
| 6 | Spark Fundamentals | [lesson_06_spark_basics.ipynb](./module_03_data_engineering/lesson_06_spark_basics.ipynb) | Distributed processing | "Pandas vs Spark?" | 🔄 Creating |
| 7 | Prefect Orchestration | [lesson_07_workflow_orchestration_prefect.ipynb](./module_03_data_engineering/lesson_07_workflow_orchestration_prefect.ipynb) | DAGs, scheduling | "Orchestrate daily retraining" | 🔄 Creating |

**Module README**: [module_03_data_engineering/README.md](./module_03_data_engineering/README.md) ✅

**Exercises**: [ex03_data_engineering.ipynb](./module_03_data_engineering/exercises/ex03_data_engineering.ipynb)

**Project**: [End-to-End Data Pipeline](./module_03_data_engineering/projects/end_to_end_data_pipeline/)

---

## 🧠 Module 4: Model Development & Optimization

**Location**: `module_04_model_development/`  
**Duration**: 4 weeks  
**Topics**: Tuning, Pruning, Distillation, Quantization, ONNX  
**Status**: 🟡 In Progress

| # | Lesson | File | Key Topics | Interview Focus |
|---|--------|------|------------|-----------------|
| 1 | Model Selection | [lesson_01_model_selection.ipynb](./module_04_model_development/lesson_01_model_selection.ipynb) | Selection strategies | "How choose models?" | 🔄 Creating |
| 2 | Hyperparameter Tuning | [lesson_02_hyperparameter_tuning.ipynb](./module_04_model_development/lesson_02_hyperparameter_tuning.ipynb) | Bayesian opt, Optuna | "Efficient tuning?" | 🔄 Creating |
| 3 | Transfer Learning | [lesson_03_transfer_learning.ipynb](./module_04_model_development/lesson_03_transfer_learning.ipynb) | Fine-tuning, layer freezing | "When use transfer learning?" | 🔄 Creating |
| 4 | Model Pruning | [lesson_04_model_pruning.ipynb](./module_04_model_development/lesson_04_model_pruning.ipynb) | Structured/unstructured | "What is pruning?" | 🔄 Creating |
| 5 | Knowledge Distillation | [lesson_05_knowledge_distillation.ipynb](./module_04_model_development/lesson_05_knowledge_distillation.ipynb) | Teacher-student | "Explain distillation" | 🔄 Creating |
| 6 | Quantization | [lesson_06_quantization.ipynb](./module_04_model_development/lesson_06_quantization.ipynb) | INT8, FP16, QAT | "When use quantization?" | 🔄 Creating |
| 7 | ONNX Basics | [lesson_07_onnx_basics.ipynb](./module_04_model_development/lesson_07_onnx_basics.ipynb) | Model conversion | "Why ONNX?" | 🔄 Creating |
| 8 | ONNX Runtime | [lesson_08_onnx_runtime.ipynb](./module_04_model_development/lesson_08_onnx_runtime.ipynb) | Production inference | "Optimize inference latency" | 🔄 Creating |

**Module README**: [module_04_model_development/README.md](./module_04_model_development/README.md) ✅
**Exercises**: [ex04_model_development.ipynb](./module_04_model_development/exercises/ex04_model_development.ipynb)

**Project**: [Optimized Model Pipeline](./module_04_model_development/projects/optimized_model_pipeline/)

## 🖼️ Capstone Project: CV MLOps Pipeline
**Location**: `cv_mlops_project/`
**Goal**: End-to-End Object Detection (YOLOv8) with DVC, Hydra, W&B, and ONNX.
**Notebooks**:
1. [Data Setup (DVC)](./cv_mlops_project/notebooks/01_data_setup_dvc.ipynb)
2. [Training (Hydra+W&B)](./cv_mlops_project/notebooks/02_training_tracking.ipynb)
3. [Optimization (ONNX)](./cv_mlops_project/notebooks/03_optimization_onnx.ipynb)

---

## 🛠️ Module 4b: Advanced Tooling (Bonus)

**Location**: `module_04_advanced_tooling/`  
**Duration**: 2 weeks  
**Topics**: Hydra, Poetry, Pre-commit, PyTest, Cookiecutter, Typer  
**Status**: ✅ Complete

| # | Lesson | File | Key Topics | Interview Focus |
|---|--------|------|------------|-----------------|
| 1 | Hydra Configs | [lesson_01_hydra_config.ipynb](./module_04_advanced_tooling/lesson_01_hydra_config.ipynb) | Hierarchical config, OmegaConf | "Argparse vs Configs?" |
| 2 | Poetry Dependency | [lesson_02_dependency_management.ipynb](./module_04_advanced_tooling/lesson_02_dependency_management.ipynb) | pyproject.toml, locking | "Reproducible environments?" |
| 3 | Code Quality | [lesson_03_code_quality.ipynb](./module_04_advanced_tooling/lesson_03_code_quality.ipynb) | Black, Ruff, Pre-commit | "Enforcing code style?" |
| 4 | Testing ML | [lesson_04_testing_ml.ipynb](./module_04_advanced_tooling/lesson_04_testing_ml.ipynb) | PyTest, Data vs Code tests | "How to test ML models?" |
| 5 | Project Templates | [lesson_05_project_templates.ipynb](./module_04_advanced_tooling/lesson_05_project_templates.ipynb) | Cookiecutter Data Science | "Structuring new projects" |
| 6 | CLI Building | [lesson_06_cli_building.ipynb](./module_04_advanced_tooling/lesson_06_cli_building.ipynb) | Typer, Type hints | "Building ML tools" |

**Exercises**: [ex04b_advanced_tooling.ipynb](./module_04_advanced_tooling/exercises/ex04b_advanced_tooling.ipynb)

---

## 🚀 Module 5: Model Deployment

**Location**: `module_05_deployment/`  
**Duration**: 4 weeks  
**Topics**: FastAPI, Docker, Kubernetes, Cloud Patterns, Load Testing  
**Status**: ✅ Complete

| # | Lesson | File | Key Topics | Interview Focus |
|---|--------|------|------------|-----------------|
| 1 | Serialization | [lesson_01_serialization.ipynb](./module_05_deployment/lesson_01_serialization.ipynb) | Pickle vs Safetensors, Security | "Secure model loading?" |
| 2 | FastAPI Basics | [lesson_02_fastapi_basics.ipynb](./module_05_deployment/lesson_02_fastapi_basics.ipynb) | ASGI, Routes, Swagger UI | "Flask vs FastAPI?" |
| 3 | Data Validation | [lesson_03_pydantic_validation.ipynb](./module_05_deployment/lesson_03_pydantic_validation.ipynb) | Pydantic, Type Hints | "Validate API inputs?" |
| 4 | Docker Basics | [lesson_04_docker_basics.ipynb](./module_05_deployment/lesson_04_docker_basics.ipynb) | Dockerfile, Layers, Caching | "Container vs VM?" |
| 5 | Docker Compose | [lesson_05_docker_compose.ipynb](./module_05_deployment/lesson_05_docker_compose.ipynb) | Multi-container, Networking | "Local dev stack?" |
| 6 | Kubernetes Basics | [lesson_06_kubernetes_basics.ipynb](./module_05_deployment/lesson_06_kubernetes_basics.ipynb) | Pods, Deployments, Services | "What is a Pod?" |
| 7 | Cloud Patterns | [lesson_07_cloud_patterns.ipynb](./module_05_deployment/lesson_07_cloud_patterns.ipynb) | EC2 vs K8s vs Lambda | "Serverless for ML?" |
| 8 | Serving Patterns | [lesson_08_serving_patterns.ipynb](./module_05_deployment/lesson_08_serving_patterns.ipynb) | Online vs Batch vs Stream | "Fraud detection design?" |
| 9 | Load Testing | [lesson_09_load_testing.ipynb](./module_05_deployment/lesson_09_load_testing.ipynb) | Locust, RPS, P99 Latency | "Test API limits?" |

**Module README**: [module_05_deployment/README.md](./module_05_deployment/README.md) ✅

**Project**: [Production Deployment](./module_05_deployment/projects/production_deployment/)

---

## 📊 Module 6: Monitoring, Observability & CI/CD

**Location**: `module_06_monitoring_cicd/`  
**Duration**: 4 weeks  
**Topics**: Drift, Evidently, Prometheus, Grafana, GitHub Actions  
**Status**: ✅ Complete

| # | Lesson | File | Key Topics | Interview Focus |
|---|--------|------|------------|-----------------|
| 1 | Drift Concepts | [lesson_01_drift_concepts.ipynb](./module_06_monitoring_cicd/lesson_01_drift_concepts.ipynb) | Data vs Concept Drift, KS-Test | "Data Drift vs Concept Drift?" | ✅ Ready |
| 2 | Evidently AI | [lesson_02_evidently_ai.ipynb](./module_06_monitoring_cicd/lesson_02_evidently_ai.ipynb) | Automated drift reports, JSON export | "Automating monitoring?" | ✅ Ready |
| 3 | Prometheus & Grafana | [lesson_03_prometheus_grafana.ipynb](./module_06_monitoring_cicd/lesson_03_prometheus_grafana.ipynb) | System metrics, custom exporters | "Pull vs Push monitoring?" | ✅ Ready |
| 4 | GitHub Actions (CI) | [lesson_04_github_actions_ci.ipynb](./module_06_monitoring_cicd/lesson_04_github_actions_ci.ipynb) | Unit tests, Linting, Workflow YAML | "How to test ML models?" | ✅ Ready |
| 5 | CD for ML & GitOps | [lesson_05_cd_for_ml.ipynb](./module_06_monitoring_cicd/lesson_05_cd_for_ml.ipynb) | Docker Build/Push, Blue/Green, ArgoCD | "Deployment strategies?" | ✅ Ready |

**Module README**: [module_06_monitoring_cicd/README.md](./module_06_monitoring_cicd/README.md) ✅

**Project**: [Full CI/CD Pipeline](./module_06_monitoring_cicd/projects/full_cicd_pipeline/)

---

## 🏆 Capstone Project

**Location**: `capstone_project/`  
**Duration**: 3 weeks  
**Status**: 🟡 Template In Progress

Apply everything you've learned to build a complete production ML system:

- **Overview**: [capstone_project/README.md](./capstone_project/README.md) ✅
- **Code Template**: 🔄 Creating
- **Evaluation Rubric**: Included in README

**Components**:
1. Data pipeline with DVC + Feast
2. Model training with MLflow/W&B
3. Model optimization (ONNX)
4. Deployment (FastAPI + Docker + K8s + EKS)
5. Monitoring (Evidently + Prometheus + Grafana)
6. CI/CD (GitHub Actions + GitOps)

---

## 🔍 Find Content By Topic

### Interview Question Type

**System Design**:
- Module 3: Lesson 2 (ETL pipeline design)
- Module 5: Lesson 3 (API design)
- Module 6: Lesson 6-9 (CI/CD design)

**Technical Depth**:
- Module 2: All lessons (reproducibility)
- Module 4: Lessons 4-8 (optimization)
- Module 5: Lessons 1-4 (deployment)

**Behavioral/Process**:
- Module 1: All lessons (foundations)
- Module 2: Lesson 1, 8 (best practices)
- Module 6: Lessons 1-2 (monitoring approach)

### By Tool

- **DVC**: Module 2, Lesson 2
- **MLflow**: Module 2, Lessons 3-4
- **W&B**: Module 2, Lessons 5-7
- **Feast**: Module 3, Lesson 5
- **Spark**: Module 3, Lesson 6
- **Prefect**: Module 3, Lesson 7
- **ONNX**: Module 4, Lessons 7-8
- **FastAPI**: Module 5, Lessons 2-3
- **Docker**: Module 5, Lessons 5-6
- **Kubernetes**: Module 5, Lessons 7-8
- **AWS**: Module 5, Lessons 9-12
- **Evidently**: Module 6, Lesson 3
- **Prometheus/Grafana**: Module 6, Lesson 4
- **GitHub Actions**: Module 6, Lesson 8

---

## 📊 Learning Progress Tracker

Create a copy of this checklist to track your progress:

```markdown
## My Progress

### Module 1: Foundations ☐ 
- ☐ Lesson 1: Intro to MLOps
- ☐ Lesson 2: MLOps vs DevOps
- ☐ Lesson 3: ML Lifecycle

### Module 2: Reproducibility ☐
- ☐ All 8 lessons
- ☐ Reproducible pipeline project

### Module 3: Data Engineering ☐
- ☐ All 7 lessons
- ☐ Data pipeline project

### Module 4: Model Optimization ☐
- ☐ All 8 lessons
- ☐ Optimization project

### Module 5: Deployment ☐
- ☐ All 12 lessons
- ☐ Deployment project

### Module 6: Monitoring & CI/CD ☐
- ☐ All 9 lessons
- ☐ CI/CD project

### Capstone ☐
- ☐ Complete production system
```

---

## 🎯 Recommended Learning Paths

### **Path 1: Full Sequential** (26 weeks)
Follow modules 1 → 2 → 3 → 4 → 5 → 6 → Capstone

### **Path 2: Interview Sprint** (8 weeks - core topics)
1. Module 1 → Module 2 (Weeks 1-3)
2. Module 3: Lessons 2, 4, 5 (Week 4)
3. Module 4: Lessons 2, 5, 6 (Week 5)
4. Module 5: Lessons 1-3, 5-6 (Weeks 6-7)
5. Module 6: Lessons 1-3, 6-8 (Week 8)

### **Path 3: Topic-Focused**
Jump to specific modules based on interview focus:
- **Data Engineering role**: Modules 3, 6
- **ML Engineering role**: Modules 2, 4, 5
- **Research Scientist**: Modules 2, 4

---

## 📞 Quick Reference

- **Issues/Questions**: Review module READMEs first
- **Setup Problems**: Check [installation_guide.md](./tools_and_setup/installation_guide.md)
- **External Resources**: [reference_links.md](./resources/reference_links.md)
- **Cheatsheets**: `resources/cheatsheets/`

---

**Last Updated**: February 2, 2026  
**Total Lessons**: 61+  
**Total Duration**: 26 weeks (full program)

**Happy Learning! Jump anywhere you want! 🚀**
