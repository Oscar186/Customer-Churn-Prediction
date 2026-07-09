# Customer Churn Prediction System

Production-grade ML project built using Python, Scikit-learn, FastAPI, PostgreSQL, Docker, MLflow, and CI/CD.

## Goal

Predict customer churn and expose the model through a REST API.

## Roadmap

- [x] Phase 01 - Project Setup
- [x] Phase 02 - Data Ingestion & Validation
- [ ] Phase 03 - Data Cleaning & EDA
- [ ] Phase 04 - Feature Engineering
- [ ] Phase 05 - Model Training
- [ ] Phase 06 - Model Evaluation
- [ ] Phase 07 - MLflow Integration
- [ ] Phase 08 - FastAPI
- [ ] Phase 09 - Docker
- [ ] Phase 10 - Cloud Deployment
- [ ] Phase 11 - Monitoring

## Tech Stack

- Python 3.11
- Pandas
- NumPy
- PyYAML
- Logging
- Git
- GitHub

Upcoming:

- Scikit-learn
- MLflow
- FastAPI
- Docker
- PostgreSQL
- Airflow

# Customer Churn Prediction

## 🚀 Project Status

## Project Progress

### ✅ Phase 01: Project Setup
- Initialized project structure
- Configured logging and exception handling
- Organized directories for components, artifacts, configs, and utilities

### ✅ Phase 02: Data Ingestion & Validation
- Implemented modular data ingestion component
- Added schema-based data validation
- Introduced typed configuration and artifact entities
- Centralized configuration management

### ✅ Phase 03: Exploratory Data Analysis
- Performed univariate and bivariate analysis
- Conducted statistical validation using:
  - Chi-Square Test
  - Correlation Analysis
  - Variance Inflation Factor (VIF)
- Identified significant features and multicollinearity

### 🚧 Phase 04: Data Transformation (In Progress)
- Built preprocessing pipeline using:
  - StandardScaler
  - OneHotEncoder
  - ColumnTransformer
- Implemented train-test split with stratification
- Added serialization utilities for preprocessors and NumPy arrays
- Refactored project into a modular, artifact-driven pipeline architecture

## Project Structure

```text
customer-churn-prediction/
│
├── app/                             # FastAPI application
│
├── artifacts/                       # Generated artifacts
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
│   ├── Raw/                         # Original dataset
│   ├── Interim/                     # Intermediate datasets
│   └── Processed/                   # Processed datasets
│
├── logs/                            # Application logs
│
├── models/                          # Saved ML models
│
├── notebooks/                       # Jupyter notebooks (EDA & experiments)
│
├── reports/
│   └── figures/                     # EDA visualizations
│
├── scripts/                         # Utility scripts
│
├── src/
│   ├── Components/                  # Core ML components
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   │
│   ├── Config/                      # Configuration manager
│   │   └── configuration.py
│   │
│   ├── Constants/                   # Project constants
│   │   └── __init__.py
│   │
│   ├── Entity/                      # Config & artifact dataclasses
│   │   ├── config_entity.py
│   │   └── artifact_entity.py
│   │
│   ├── Pipeline/                    # Training & prediction pipelines
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
│   │
│   ├── Utils/                       # Common helper functions
│   │   └── common.py
│   │
│   ├── logger.py
│   ├── exception.py
│   └── __init__.py
│
├── temp/                            # Temporary files
│
├── tests/                           # Unit tests
│
├── main.py
├── requirements.txt
└── README.md
```


## 🚀 Features Implemented

### 📌 Project Architecture

* Modular, production-ready ML pipeline architecture
* Configuration-driven design using YAML files
* Centralized configuration management
* Strongly typed configuration and artifact entities
* Comprehensive logging and custom exception handling
* Organized project structure following software engineering best practices

### 📥 Data Ingestion

* Automated dataset loading
* Dataset path validation
* Artifact-based data ingestion workflow

### ✅ Data Validation

* Schema-based dataset validation
* Automatic column consistency checks
* Validation status tracking through pipeline artifacts

### 📊 Exploratory Data Analysis (EDA)

* Dataset overview and quality assessment
* Missing value analysis
* Duplicate record detection
* Data type analysis
* Univariate analysis
* Bivariate analysis
* Distribution analysis for numerical features
* Category-wise churn analysis
* Correlation analysis
* Outlier detection

### 📈 Statistical Analysis

* Chi-Square Test for categorical feature significance
* Correlation Matrix for numerical features
* Variance Inflation Factor (VIF) for multicollinearity detection
* Statistical feature selection and validation

### ⚙️ Data Transformation

* Automated train-test splitting with stratification
* Feature preprocessing using Scikit-learn Pipelines
* Numerical feature scaling using StandardScaler
* Categorical feature encoding using OneHotEncoder
* ColumnTransformer-based preprocessing
* Serialization of preprocessing pipeline
* Processed dataset export as NumPy arrays

### 🛠 Utility Module

* YAML configuration reader
* CSV read/write utilities
* Object serialization using Joblib
* NumPy array persistence
* Directory management utilities
* Reusable helper functions for pipeline components

### 📝 Logging & Exception Handling

* Centralized logging framework
* Custom exception handling
* Component-level execution tracking
* Debug-friendly pipeline logs

### 🚧 Upcoming Features

* Model Training
* Model Evaluation
* Prediction Pipeline
* FastAPI REST API
* Docker Containerization
* CI/CD Integration
* Model Deployment
* Monitoring & Logging Enhancements
