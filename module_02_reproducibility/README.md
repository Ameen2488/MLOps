# Module 2: Reproducibility & Versioning

**Master reproducibility and versioning - critical skills for production ML systems and Senior DS interviews.**

---

## 🎯 Module Overview

**Duration**: 3 weeks  
**Difficulty**: Intermediate  
**Prerequisites**: Module 1 completed, Git basics, Python proficiency

This module covers one of the **most critical aspects** of MLOps that separates junior from senior data scientists: the ability to create reproducible, versioned ML workflows.

In interviews at top companies (Google, Meta, Amazon, etc.), you'll be asked about:
- "How do you ensure your experiments are reproducible?"
- "How do you track and compare multiple model versions?"
- "What's your approach to data versioning?"
- "How do you collaborate on ML projects with your team?"

This module gives you production-grade answers with hands-on implementation.

---

## 📖 Learning Objectives

By the end of this module, you will:

✅ Implement deterministic ML pipelines  
✅ Version control data, models, and experiments  
✅ Use DVC for large-scale data versioning  
✅ Track experiments with MLflow  
✅ Use Weights & Biases for advanced experiment management  
✅ Build complete model registries  
✅ Compare MLflow vs W&B for different use cases  
✅ Answer senior-level interview questions on reproducibility  

---

## 📚 Lessons

### **Lesson 1: Why Reproducibility Matters**
📓 [lesson_01_why_reproducibility.ipynb](./lesson_01_why_reproducibility.ipynb)

**Topics Covered**:
- What is reproducibility and why it's critical
- Real-world reproducibility failures and their costs
- Debugging without reproducibility
- Regulatory compliance (FDA, finance, healthcare)
- Collaboration challenges
- Interview question deep-dives

**Key Concepts**:
- Deterministic vs stochastic processes
- Sources of non-determinism in ML
- Reproducibility vs replicability
- Production vs research reproducibility

**Duration**: ~2 hours with exercises

---

### **Lesson 2: Git and DVC Fundamentals**
📓 [lesson_02_git_and_dvc.ipynb](./lesson_02_git_and_dvc.ipynb)

**Topics Covered**:
- Git for ML projects (advanced patterns)
- Why Git isn't enough for ML
- DVC architecture and workflow
- Tracking datasets with DVC
- Remote storage configuration (S3, GCS, Azure)
- Data pipelines with DVC
- Team collaboration with DVC

**Key Concepts**:
- Git LFS vs DVC
- Content-addressable storage
- DVC cache management
- .dvc file format
- dvc.yaml pipelines

**Hands-on**:
- Set up DVC with cloud storage
- Version control a dataset
- Create reproducible data pipeline

**Duration**: ~4 hours with exercises

---

### **Lesson 3: MLflow Basics - Experiment Tracking**
📓 [lesson_03_mlflow_basics.ipynb](./lesson_03_mlflow_basics.ipynb)

**Topics Covered**:
- MLflow architecture (Tracking, Projects, Models, Registry)
- Setting up MLflow tracking server
- Logging parameters, metrics, and artifacts
- Organizing experiments and runs
- Comparing runs
- MLflow UI deep dive

**Key Concepts**:
- Run context and nesting
- Autologging
- Artifact storage
- Backend stores vs artifact stores
- MLflow server deployment

**Hands-on**:
- Track scikit-learn experiments
- Compare hyperparameter runs
- Log custom metrics and artifacts

**Duration**: ~3 hours with exercises

---

### **Lesson 4: MLflow with PyTorch - Advanced Patterns**
📓 [lesson_04_mlflow_pytorch.ipynb](./lesson_04_mlflow_pytorch.ipynb)

**Topics Covered**:
- Deep learning experiment tracking
- Logging model checkpoints
- Tracking training curves
- Distributed training considerations
- GPU metrics logging
- Model signatures and input examples
- Custom metrics for deep learning

**Key Concepts**:
- PyTorch Lightning + MLflow
- Checkpoint management
- Hyperparameter optimization with Optuna + MLflow
- Resource usage tracking

**Hands-on**:
- Track PyTorch CNN training
- Implement early stopping with MLflow
- Log model with custom inference logic

**Duration**: ~4 hours with exercises

---

### **Lesson 5: Weights & Biases - Introduction**
📓 [lesson_05_wandb_intro.ipynb](./lesson_05_wandb_intro.ipynb)

**Topics Covered**:
- W&B vs MLflow philosophy
- W&B architecture and components
- Setting up W&B projects
- Real-time visualization
- Team collaboration features
- W&B Sweeps for hyperparameter tuning

**Key Concepts**:
- wandb.init() and configuration
- Logging best practices
- W&B Tables for dataset versioning
- Artifact lineage
- Report generation

**Hands-on**:
- Set up W&B project
- Track first experiment
- Create comparison reports

**Duration**: ~3 hours with exercises

---

### **Lesson 6: W&B with scikit-learn - Complete Workflow**
📓 [lesson_06_wandb_sklearn.ipynb](./lesson_06_wandb_sklearn.ipynb)

**Topics Covered**:
- End-to-end ML workflow with W&B
- Dataset versioning with Artifacts
- Model versioning and registry
- Hyperparameter sweeps
- Cross-validation tracking
- Feature importance logging
- Model cards and documentation

**Key Concepts**:
- W&B Artifacts API
- Sweep configuration
- Model linking and aliasing
- Production model promotion

**Hands-on**:
- Build complete classification pipeline
- Version datasets and models
- Run hyperparameter sweep
- Promote model to production

**Duration**: ~4 hours with exercises

---

### **Lesson 7: W&B with PyTorch - Deep Learning Workflows**
📓 [lesson_07_wandb_pytorch.ipynb](./lesson_07_wandb_pytorch.ipynb)

**Topics Covered**:
- Deep learning experiment tracking
- Real-time training metrics
- System metrics (GPU, memory)
- Gradient tracking and histogram logging
- Image logging for computer vision
- Model checkpoint management
- Multi-run comparison and analysis

**Key Concepts**:
- wandb.watch() for gradient tracking
- Media logging (images, audio, video)
- Custom charts and visualizations
- Distributed training integration

**Hands-on**:
- Track CNN training with visualizations
- Log training images and predictions
- Compare multiple architectures
- Implement model checkpointing

**Duration**: ~4 hours with exercises

---

### **Lesson 8: MLflow vs W&B - Complete Comparison**
📓 [lesson_08_mlflow_vs_wandb.ipynb](./lesson_08_mlflow_vs_wandb.ipynb)

**Topics Covered**:
- Feature-by-feature comparison
- When to use MLflow
- When to use W&B
- Using both together
- Migration strategies
- Cost considerations
- Enterprise deployment patterns

**Key Concepts**:
- Self-hosted vs SaaS trade-offs
- Team collaboration features
- Integration ecosystems
- Scalability considerations

**Interview Preparation**:
- "Which experiment tracking tool would you choose and why?"
- "How would you migrate from X to Y?"
- "What are the limitations of each approach?"

**Duration**: ~3 hours with exercises

---

## 🛠️ Hands-on Projects

### **Project 1: Reproducible ML Pipeline**
📂 [projects/reproducible_pipeline/](./projects/reproducible_pipeline/)

Build a complete, reproducible ML pipeline demonstrating all concepts:

**Requirements**:
- Data versioning with DVC
- Experiment tracking (MLflow or W&B)
- Deterministic training
- Model registry
- Complete documentation
- Reproducibility tests

**Skills Practiced**:
- End-to-end workflow design
- Tool integration
- Best practices implementation
- Documentation for reproducibility

**Time Estimate**: 8-10 hours

---

## 📝 Interview Preparation

### **Common Senior DS Interview Questions**

This module prepares you to answer:

1. **Reproducibility**:
   - "How do you ensure your ML experiments are reproducible?"
   - "What are the main challenges to reproducibility in ML?"
   - "How would you debug a model that works in development but fails in production?"

2. **Versioning**:
   - "How do you version control datasets that are too large for Git?"
   - "Explain your approach to model versioning."
   - "How do you track which model version is deployed in production?"

3. **Experiment Tracking**:
   - "How do you track and compare hundreds of experiments?"
   - "What metrics do you track beyond model performance?"
   - "How do you share experiment results with your team?"

4. **Tool Selection**:
   - "MLflow vs Weights & Biases - which would you choose?"
   - "How would you set up experiment tracking for a team of 10 data scientists?"
   - "What's your experience with [specific tool]?"

---

## ✅ Module Completion Checklist

- [ ] Complete all 8 lessons with exercises
- [ ] Build reproducible pipeline project
- [ ] Set up DVC with cloud storage
- [ ] Track at least 10 experiments with MLflow
- [ ] Track at least 10 experiments with W&B
- [ ] Create comparison report
- [ ] Practice interview questions
- [ ] Review and consolidate notes

---

## 🎓 Assessment

### **Self-Check Questions**:

1. What are the three main challenges to reproducibility in ML?
2. How does DVC differ from Git LFS?
3. Explain the MLflow architecture (4 components).
4. What's the difference between parameters and metrics in experiment tracking?
5. When would you choose MLflow over W&B?
6. How do you ensure deterministic training in PyTorch?
7. What's the purpose of a model registry?
8. How do you version a 100GB dataset?

### **Practical Assessment**:
Build a project that demonstrates:
- Data versioning
- Experiment tracking
- Model registry
- Reproducible training
- Complete documentation

---

## 📚 Additional Resources

**Must-Read**:
- [Daily Dose of DS - Parts 3-4](https://www.dailydoseofds.com/mlops-crash-course-part-3/)
- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [W&B Best Practices](https://docs.wandb.ai/guides/track/best-practices)
- [DVC Documentation](https://dvc.org/doc)

**Deep Dives**:
- Hidden Technical Debt in ML Systems
- Reproducibility in ML (paper collection)
- Production ML Best Practices

---

## ➡️ Next Steps

Once you've mastered this module:

👉 Proceed to [Module 3: Data & Pipeline Engineering](../module_03_data_engineering/)

In Module 3, you'll learn to build production data pipelines with ETL, feature stores, Spark, and workflow orchestration.

---

## 💼 Interview Success Tips

**What Senior DS Interviewers Look For**:

1. **Practical Experience**: Can you actually implement these tools?
2. **Trade-off Understanding**: Do you know when to use what?
3. **Production Thinking**: Beyond notebooks - how do you deploy this?
4. **Team Collaboration**: How do you enable team productivity?
5. **Best Practices**: Are you aware of industry standards?

**This module gives you hands-on experience with all of these!**

---

**Ready to become a reproducibility expert? Let's dive in! 🚀**
