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
- [x] Phase 06 - Model Evaluation
- [x] Phase 07 - Model Pusher & Model Registry
- [x] Phase 08 - Prediction Pipeline & FastAPI
- [x] Phase 09 - MLflow Integration
- [x] Phase 10 - Dockerization
- [ ] Phase 11 - PostgreSQL Integration
- [ ] Phase 12 - Airflow Orchestration
- [ ] Phase 13 - Cloud Deployment
- [ ] Phase 14 - Monitoring & CI/CD

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
- FastAPI
- Uvicorn
- Pydantic
- MLflow
- Docker
- Git
- GitHub

## Upcoming

- Airflow
- PostgreSQL
- CI/CD
- Cloud Deployment
- Monitoring

---

# 🚀 Project Progress

## ✅ Phase 01: Project Setup

- Initialized a production-ready project structure.
- Configured centralized logging.
- Implemented custom exception handling.
- Organized project into modular components, configurations, artifacts, utilities, and pipelines.

---

## ✅ Phase 02: Data Ingestion & Validation

- Implemented modular Data Ingestion component.
- Built schema-based Data Validation component.
- Introduced strongly typed Configuration entities.
- Introduced Artifact entities for pipeline communication.
- Centralized configuration management using YAML.

---

## ✅ Phase 03: Exploratory Data Analysis

- Dataset quality assessment.
- Missing value analysis.
- Duplicate record detection.
- Univariate analysis.
- Bivariate analysis.
- Outlier analysis.
- Correlation analysis.
- Chi-Square Test.
- Variance Inflation Factor (VIF).
- Feature significance analysis.
- Business insights generation.

---

## ✅ Phase 04: Data Transformation

- Automated train-test split using stratified sampling.
- Built preprocessing pipeline using Scikit-learn Pipeline.
- Missing value handling using SimpleImputer.
- Numerical feature scaling using StandardScaler.
- Categorical encoding using OneHotEncoder.
- Unified preprocessing using ColumnTransformer.
- Serialized preprocessing pipeline using Joblib.
- Saved processed datasets as NumPy arrays.
- Integrated transformation into modular training pipeline.

---

## ✅ Phase 05: Model Training

- Implemented modular Model Trainer component.
- Automated loading of transformed training and testing datasets.
- Built reusable multi-model training framework.
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
- Automatically selected the best-performing model based on ROC-AUC.
- Serialized the trained model using Joblib.
- Generated model performance report.
- Saved evaluation metrics as JSON.
- Integrated Model Trainer into the end-to-end training pipeline.

---

## ✅ Phase 06: Model Evaluation

- Implemented modular Model Evaluation component.
- Loaded transformed test dataset for candidate model validation.
- Loaded trained candidate model from persisted artifacts.
- Evaluated model performance using:
  - Accuracy
  - Precision
  - Recall
  - F1 Score
  - ROC-AUC Score
- Generated evaluation report as YAML.
- Introduced Model Evaluation Artifact for downstream pipeline communication.
- Implemented configuration-driven evaluation workflow.
- Integrated Model Evaluation into the end-to-end training pipeline.
- Established foundation for production model comparison and deployment workflow.

---

## ✅ Phase 07: Model Pusher & Model Registry

- Implemented modular Model Pusher component
- Promoted only accepted models to production
- Created a dedicated production model directory
- Copied trained model to the production registry
- Copied preprocessing pipeline for inference
- Added Model Pusher artifact for pipeline communication
- Integrated Model Pusher into the end-to-end training pipeline
- Established the foundation for model versioning and deployment

---

## ✅ Phase 08: Prediction Pipeline & FastAPI

- Built reusable Prediction Pipeline
- Created CustomerData class for inference
- Automatic preprocessing using saved preprocessing pipeline
- Production model loading
- FastAPI REST API
- Request validation using Pydantic
- JSON prediction responses
- Probability prediction support
- Health Check endpoint
- Interactive Swagger Documentation

---

## ✅ Phase 09: MLFlow Integration

- Integrated MLflow Experiment Tracking
- Automatic experiment creation
- Automatic run tracking
- Logged model metrics
- Logged training parameters
- Logged model artifacts
- Logged trained models
- Added model signature
- Added input example
- Added experiment tags
- Recorded training execution time

---

## ✅ Phase 10: Dockerization

- Dockerfile created
- Python slim base image
- Multi-stage dependency installation
- Containerized FastAPI application
- Production-ready startup command
- Port mapping
- Environment isolation
- Reproducible deployment

---

# 🔄 Training Pipeline Workflow

```text
Dataset
   │
   ▼
Data Ingestion
   │
   ▼
Data Validation
   │
   ▼
EDA
   │
   ▼
Data Transformation
   │
   ▼
Model Training
   │
   ▼
MLflow Logging
   │
   ▼
Model Evaluation
   │
   ▼
Model Pusher
   │
   ▼
Production Models
   │
   ▼
Prediction Pipeline
   │
   ▼
FastAPI
   │
   ▼
Docker Container
```

---

# 📂 Project Structure

```text
customer-churn-prediction/
│
├── app/                             # FastAPI application
|   ├── __init__.py
|   ├── main.py
|   └── schema.py
│
├── artifacts/                       # Generated pipeline artifacts
|   ├── data_ingestion/
|   ├── data_validation/
|   ├── data_transformation/
|   ├── model_trainer/
|   └── model_evaluation/
│
├── configs/                         # Configuration files
│   ├── config.yaml
│   ├── params.yaml
│   └── schema.yaml
│
├── data/
│   ├── Raw/
│   ├── Interim/
│   └── Processed/
│
├── logs/
│
├── production_models/
│   ├── preprocessor.pkl
│   └── model.pkl
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
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
|   |   ├── model_evaluation.py|  
│   │   └── model_pusher.py
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
|
├── templates/
│   └── index.html
|
├── tests/
│   └── tests_prediction.py
|
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

## 🚀 Model Evaluation & Model Registry

## 📊 Model Evaluation

- Candidate model evaluation
- Classification metric calculation
- Acceptance decision logic
- Evaluation report generation
- YAML-based evaluation artifact
- Production model comparison foundation

## 🚀 Model Registry & Deployment

- Model promotion workflow
- Production model registry
- Automated model pushing
- Artifact-driven deployment
- Persistent production model storage

---

## 🚀 Prediction API

- FastAPI REST API
- Health Check Endpoint
- Prediction Endpoint
- Probability Prediction
- Request Validation
- Swagger Documentation
- Production Model Loading

---

## 📈 MLflow

- Experiment Tracking
- Metrics Logging
- Parameters Logging
- Model Logging
- Model Signature
- Input Example
- Artifact Logging
- Run Comparison

---

## 🐳 Docker

- Containerized API
- Lightweight Python Image
- Production Startup
- Dependency Isolation

---

# 🚧 Upcoming Features

- PostgreSQL Integration
- CI/CD Pipeline
- Cloud Deployment
- Monitoring & Logging

---

## 📌 Current Status

Completed:
✅ Phase 01 → Phase 10

The project now includes a complete production-grade Machine Learning pipeline capable of:

- Data ingestion
- Data validation
- Exploratory data analysis
- Data transformation
- Model training
- Model evaluation
- Model promotion
- Production model registry
- Prediction pipeline
- REST API using FastAPI
- MLflow experiment tracking
- Docker containerization

Generated artifacts:

```text
artifacts/
├── data_ingestion/
├── data_validation/
├── data_transformation/
├── model_trainer/
├── model_evaluation/
└── model_pusher/

production_models/
├── model.pkl
└── preprocessor.pkl
```

The project is now deployment-ready.