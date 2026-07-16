# Customer Churn Prediction System

A production-ready Machine Learning project that predicts customer churn using a modular, artifact-driven pipeline architecture. The project is built with Python and Scikit-learn following software engineering best practices, making it scalable, maintainable, and deployment-ready.

---

# 🎯 Project Goal

Build an end-to-end Machine Learning system capable of predicting customer churn and exposing predictions through a REST API using FastAPI. The project follows a production-oriented architecture with modular pipeline components, configuration management, artifact tracking, logging, and model versioning.

---

# 🛣️ Roadmap

- [x] Phase 01 - Project Setup
- [x] Phase 02 - Data Ingestion & Validation
- [x] Phase 03 - Exploratory Data Analysis
- [x] Phase 04 - Data Transformation
- [x] Phase 05 - Model Training
- [ ] Phase 06 - Model Evaluation
- [ ] Phase 07 - MLflow Integration
- [ ] Phase 08 - FastAPI Integration
- [ ] Phase 09 - Dockerization
- [ ] Phase 10 - Cloud Deployment
- [ ] Phase 11 - Monitoring & CI/CD

---

# 💻 Tech Stack

## Currently Used

- Python 3.11
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- PyYAML
- Joblib
- Logging
- Git
- GitHub

## Upcoming

- FastAPI
- PostgreSQL
- MLflow
- Docker
- Airflow
- CI/CD
- Cloud Deployment

---

# 🚀 Project Progress

## ✅ Phase 01: Project Setup

- Initialized a production-ready project structure
- Configured centralized logging
- Implemented custom exception handling
- Organized project into modular components, configurations, artifacts, utilities, and pipelines

---

## ✅ Phase 02: Data Ingestion & Validation

- Implemented modular Data Ingestion component
- Built schema-based Data Validation component
- Introduced strongly typed Configuration entities
- Introduced Artifact entities for pipeline communication
- Centralized configuration management using YAML

---

## ✅ Phase 03: Exploratory Data Analysis

- Dataset quality assessment
- Missing value analysis
- Duplicate record detection
- Univariate analysis
- Bivariate analysis
- Outlier analysis
- Correlation analysis
- Chi-Square Test
- Variance Inflation Factor (VIF)
- Feature significance analysis
- Business insights generation

---

## ✅ Phase 04: Data Transformation

- Automated train-test split using stratified sampling
- Built preprocessing pipeline using Scikit-learn Pipeline
- Missing value handling using SimpleImputer
- Numerical feature scaling using StandardScaler
- Categorical encoding using OneHotEncoder
- Unified preprocessing using ColumnTransformer
- Serialized preprocessing pipeline using Joblib
- Saved processed datasets as NumPy arrays
- Integrated transformation into modular training pipeline

---

## ✅ Phase 05: Model Training

- Implemented modular Model Trainer component
- Automated loading of transformed training and testing datasets
- Built reusable multi-model training framework
- Trained multiple classification algorithms:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Gradient Boosting
  - AdaBoost
- Evaluated models using:
  - Accuracy
  - Precision
  - Recall
  - F1 Score
  - ROC-AUC Score
- Automatically selected the best-performing model based on ROC-AUC
- Serialized the trained model using Joblib
- Generated model performance report
- Saved evaluation metrics as JSON
- Integrated Model Trainer into the end-to-end training pipeline

---

# 🔄 Training Pipeline Workflow

```text
Raw Dataset
      │
      ▼
Data Ingestion
      │
      ▼
Data Validation
      │
      ▼
Data Transformation
      │
      ▼
Train/Test NumPy Arrays
      │
      ▼
Model Training
      │
      ▼
Best Model Selection
      │
      ▼
model.pkl
metrics.json
model_report.csv
```

---

# 📂 Project Structure

```text
customer-churn-prediction/
│
├── app/                             # FastAPI application
│
├── artifacts/                       # Generated pipeline artifacts
│   ├── data_ingestion/
│   ├── data_validation/
│   ├── data_transformation/
│   └── model_trainer/
│
├── configs/                         # Configuration files
│   ├── config.yaml
│   └── schema.yaml
│
├── data/
│   ├── Raw/
│   ├── Interim/
│   └── Processed/
│
├── logs/
│
├── models/
│
├── notebooks/
│
├── reports/
│   └── figures/
│
├── scripts/
│
├── src/
│   ├── Components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   │
│   ├── Config/
│   │   └── configuration.py
│   │
│   ├── Constants/
│   │   └── __init__.py
│   │
│   ├── Entity/
│   │   ├── config_entity.py
│   │   └── artifact_entity.py
│   │
│   ├── Pipeline/
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
│   │
│   ├── Utils/
│   │   └── common.py
│   │
│   ├── logger.py
│   ├── exception.py
│   └── __init__.py
│
├── temp/
│
├── tests/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 🚀 Features Implemented

## 📌 Project Architecture

- Production-ready modular ML pipeline
- Artifact-driven workflow
- Configuration-driven architecture
- YAML-based configuration management
- Strongly typed Configuration & Artifact entities
- Centralized logging
- Custom exception handling
- Clean separation of pipeline components

---

## 📥 Data Ingestion

- Configuration-driven dataset management
- Automated dataset ingestion
- Artifact generation
- Modular ingestion workflow

---

## ✅ Data Validation

- Schema-based validation
- Dataset column verification
- Validation artifact generation
- Pipeline-ready validation component

---

## 📊 Exploratory Data Analysis

- Dataset overview
- Missing value analysis
- Duplicate analysis
- Data type analysis
- Univariate analysis
- Bivariate analysis
- Numerical feature distributions
- Categorical feature analysis
- Churn distribution analysis
- Correlation analysis
- Outlier detection

---

## 📈 Statistical Analysis

- Chi-Square Test
- Correlation Matrix
- Variance Inflation Factor (VIF)
- Feature significance analysis
- Multicollinearity detection

---

## ⚙️ Data Transformation

- Train-test split with stratification
- Missing value imputation using SimpleImputer
- Numerical preprocessing using StandardScaler
- Categorical preprocessing using OneHotEncoder
- Unified preprocessing using ColumnTransformer
- Scikit-learn preprocessing pipeline
- Joblib serialization
- NumPy dataset export
- Artifact-driven transformation workflow

---

## 🛠 Utility Module

- YAML reader
- CSV reader & writer
- JSON persistence
- DataFrame persistence
- Object serialization
- NumPy array persistence
- Directory management
- Common reusable helper functions

---

## 📝 Logging & Exception Handling

- Centralized logging framework
- Component-level execution logs
- Custom exception handling
- Pipeline execution tracking
- Debug-friendly log messages

---

## 🤖 Model Training

- Modular Model Trainer component
- Automated loading of transformed datasets
- Multiple model training
- Model comparison framework
- Performance evaluation using multiple classification metrics
- Automatic best model selection using ROC-AUC
- Joblib model serialization
- JSON metrics generation
- CSV model performance report generation
- Artifact-driven model training workflow

---

# 🚧 Upcoming Features


- Model Evaluation
- Model Pusher
- Prediction Pipeline
- FastAPI REST API
- MLflow Experiment Tracking
- Docker Containerization
- PostgreSQL Integration
- CI/CD Pipeline
- Cloud Deployment
- Monitoring & Logging

---

# 📌 Current Status

# 📌 Current Status

**Completed:** ✅ Phase 01 → Phase 05

The project now includes a complete production-grade machine learning training pipeline capable of:

- Ingesting raw datasets
- Validating dataset schema
- Performing exploratory data analysis
- Transforming features using Scikit-learn preprocessing pipelines
- Generating train/test datasets
- Training multiple machine learning models
- Comparing model performance using classification metrics
- Selecting the best model based on ROC-AUC
- Persisting trained models and evaluation artifacts for deployment

Generated artifacts include:

```text
artifacts/
├── data_ingestion/
├── data_validation/
├── data_transformation/
│   ├── preprocessor.pkl
│   ├── train.npy
│   └── test.npy
│
└── model_trainer/
    ├── model.pkl
    ├── metrics.json
    └── model_report.csv
```

The next milestone is **Phase 06: Model Evaluation**, where the newly trained model will be validated against the currently deployed model before promotion to production.