# Module 3: Data & Pipeline Engineering

**Master production-grade data pipelines - essential for Senior DS roles handling real-world ML systems.**

---

## 🎯 Module Overview

**Duration**: 4 weeks  
**Difficulty**: Intermediate to Advanced  
**Prerequisites**: Module 1-2 completed, SQL knowledge, basic distributed computing concepts

This module covers the **most underestimated but critical skill** for senior data scientists: building robust, scalable data pipelines that power production ML systems.

**Interview Reality Check**:  
At companies like Uber, Airbnb, Netflix - **60-80% of ML engineering work is data engineering**. Senior DS roles require expertise in:
- Building ETL/ELT pipelines at scale
- Preventing data leakage
- Managing feature stores
- Processing TB-scale data with Spark
- Orchestrating complex workflows

This module makes you interview-ready and production-capable.

---

## 📖 Learning Objectives

By the end of this module, you will:

✅ Design and build production ETL/ELT pipelines  
✅ Handle sampling strategies for imbalanced data  
✅ Identify and prevent data leakage  
✅ Implement feature stores with Feast  
✅ Process big data with Apache Spark  
✅ Orchestrate workflows with Prefect  
✅ Answer advanced data engineering interview questions  

---

## 📚 Lessons

### **Lesson 1: Data Sources and Formats**
📓 [lesson_01_data_sources_formats.ipynb](./lesson_01_data_sources_formats.ipynb)

**Topics Covered**:
- Production data sources (APIs, databases, streams, files)
- Data format comparison (CSV, Parquet, Avro, JSON)
- Row-major vs column-major formats
- Compression strategies
- Performance trade-offs
- Schema evolution

**Key Concepts**:
- When to use Parquet vs CSV
- Columnar storage benefits
- Snappy vs Gzip compression
- Schema-on-read vs schema-on-write

**Real Interview Question**:  
*"You need to store 1TB of tabular data for ML. CSV or Parquet? Why?"*

**Duration**: ~3 hours

---

### **Lesson 2: ETL Pipelines - Theory and Practice**
📓 [lesson_02_etl_pipelines.ipynb](./lesson_02_etl_pipelines.ipynb)

**Topics Covered**:
- ETL vs ELT architectures
- Extract patterns (batch, streaming, CDC)
- Transform patterns (validation, cleaning, enrichment)
- Load strategies (append, upsert, overwrite)
- Pipeline testing
- Error handling and retries
- Idempotency in data pipelines

**Key Concepts**:
- Data quality checks
- Schema validation
- Incremental processing
- Backfilling strategies

**Hands-on**:
- Build multi-source ETL pipeline
- Implement data validation
- Handle schema changes
- Create idempotent transforms

**Real Interview Question**:  
*"Design an ETL pipeline for daily user activity data. How do you handle late-arriving data?"*

**Duration**: ~5 hours

---

### **Lesson 3: Sampling Strategies**
📓 [lesson_03_sampling_strategies.ipynb](./lesson_03_sampling_strategies.ipynb)

**Topics Covered**:
- Why sampling matters in ML
- Probabilistic sampling (random, stratified, weighted)
- Non-probabilistic sampling (convenience, quota)
- Class imbalance handling
- SMOTE and variants
- Under/oversampling strategies
- Focal loss
- Sampling bias and mitigation

**Key Concepts**:
- Representative sampling
- Stratification for rare classes
- Temporal sampling for time series
- Sampling for model validation

**Hands-on**:
- Implement stratified sampling
- Apply SMOTE for imbalanced data
- Compare sampling techniques
- Measure sampling bias

**Real Interview Question**:  
*"You have a fraud detection dataset with 0.1% positives. How do you handle this?"*

**Duration**: ~4 hours

---

### **Lesson 4: Data Leakage - Detection and Prevention**
📓 [lesson_04_data_leakage.ipynb](./lesson_04_data_leakage.ipynb)

**Topics Covered**:
- What is data leakage and why it's critical
- Types of leakage (target, train-test, temporal)
- Detecting leakage
- Prevention strategies
- Feature engineering without leakage
- Time-series leakage patterns
- Real-world leakage examples

**Key Concepts**:
- Target leakage
- Train-test contamination
- Look-ahead bias
- Data snooping
- Feature leakage through preprocessing

**Hands-on**:
- Identify leakage in real datasets
- Implement leak-free preprocessing
- Create temporal validation splits
- Build leakage detection tests

**Real Interview Question**:  
*"Your model has 99% accuracy but fails in production. What could be wrong?"*

**Duration**: ~4 hours

---

### **Lesson 5: Feature Stores with Feast**
📓 [lesson_05_feature_stores_feast.ipynb](./lesson_05_feature_stores_feast.ipynb)

**Topics Covered**:
- Why feature stores exist
- Feature store architecture
- Feast fundamentals
- Feature definitions and entities
- Historical vs online serving
- Point-in-time correct features
- Feature versioning
- Team collaboration benefits

**Key Concepts**:
- Training-serving skew prevention
- Feature reusability
- Feature lineage
- Materialization strategies

**Hands-on**:
- Set up Feast locally
- Define features and entities
- Implement historical retrieval
- Build online feature serving
- Prevent leakage with point-in-time joins

**Real Interview Question**:  
*"How would you ensure consistent features between training and serving?"*

**Duration**: ~5 hours

---

### **Lesson 6: Apache Spark Fundamentals**
📓 [lesson_06_spark_pyspark.ipynb](./lesson_06_spark_pyspark.ipynb)

**Topics Covered**:
- Why Spark for big data ML
- Spark architecture (driver, executors, cluster manager)
- RDDs vs DataFrames vs Datasets
- Spark transformations and actions
- Lazy evaluation
- Partitioning strategies
- Caching and persistence
- Spark SQL
- Performance tuning

**Key Concepts**:
- Wide vs narrow transformations
- Shuffle operations
- Broadcast variables
- Accumulators
- Memory management

**Hands-on**:
- Process GB-scale data with Spark
- Optimize partition count
- Implement distributed ETL
- Compare Spark vs Pandas performance

**Real Interview Question**:  
*"When would you use Spark instead of Pandas?"*

**Duration**: ~6 hours

---

### **Lesson 7: Workflow Orchestration with Prefect**
📓 [lesson_07_end_to_end_pipeline.ipynb](./lesson_07_end_to_end_pipeline.ipynb)

**Topics Covered**:
- Workflow orchestration concepts
- Prefect vs Airflow
- Prefect 2.0 architecture
- Tasks and flows
- Dependency management
- Scheduling strategies
- Error handling and retries
- Monitoring and observability
- Parameterized workflows

**Key Concepts**:
- DAG (Directed Acyclic Graph)
- Task dependencies
- Backpressure handling
- Dynamic workflows
- Deployment patterns

**Hands-on**:
- Build ML pipeline with Prefect
- Implement error handling
- Schedule daily training jobs
- Create monitoring dashboards
- Deploy to Prefect Cloud

**Real Interview Question**:  
*"How would you orchestrate a daily model retraining pipeline?"*

**Duration**: ~5 hours

---

## 🛠️ Hands-on Project

### **Project: End-to-End Data Pipeline**
📂 [projects/end_to_end_data_pipeline/](./projects/end_to_end_data_pipeline/)

Build a production-grade data pipeline:

**Requirements**:
- Multi-source data ingestion
- ETL with data quality checks
- Leak-free feature engineering
- Feature store integration (Feast)
- Spark for big data processing
- Prefect orchestration
- Complete testing suite
- Monitoring and alerting

**Skills Demonstrated**:
- System design
- Scalable architecture
- Best practices
- Production readiness

**Time Estimate**: 12-15 hours

---

## 📝 Senior DS Interview Prep

### **Data Engineering Questions You'll Master**:

1. **Pipeline Design**:
   - "Design a data pipeline for processing 1TB daily"
   - "How do you handle schema evolution?"
   - "Explain your approach to incremental processing"

2. **Data Quality**:
   - "How do you ensure data quality in production?"
   - "What tests do you write for data pipelines?"
   - "How do you detect data drift?"

3. **Leakage**:
   - "What is data leakage? Give examples"
   - "How do you prevent temporal leakage?"
   - "Explain target leakage with examples"

4. **Scalability**:
   - "When do you need Spark?"
   - "How do you optimize Spark jobs?"
   - "Pandas vs Spark - when to use what?"

5. **Feature Engineering**:
   - "What's a feature store and why use it?"
   - "How do you version features?"
   - "Explain training-serving skew"

---

## ✅ Module Completion Checklist

- [ ] Complete all 7 lessons
- [ ] Build end-to-end data pipeline project
- [ ] Process data with Spark (>1GB)
- [ ] Implement feature store with Feast
- [ ] Create orchestrated workflow with Prefect
- [ ] Practice interview questions
- [ ] Review production data engineering patterns

---

## 🎓 Assessment

**Practical Challenge**:  
Design and implement a data pipeline that:
- Handles multiple data sources
- Processes data at scale (GB+)
- Prevents data leakage
- Implements feature store
- Includes orchestration
- Has comprehensive testing

---

## 📚 Resources

- [Daily Dose of DS - Parts 5-7](https://www.dailydoseofds.com/mlops-crash-course-part-5/)
- [Feast Documentation](https://docs.feast.dev/)
- [Spark Documentation](https://spark.apache.org/docs/latest/)
- [Prefect Documentation](https://docs.prefect.io/)

---

## ➡️ Next Steps

👉 [Module 4: Model Development & Optimization](../module_04_model_development/)

Learn model optimization, pruning, quantization, and ONNX for production deployment.

---

**Master data engineering to stand out in Senior DS interviews! 🚀**
