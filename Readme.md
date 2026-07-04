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

### ✅ Phase 01 - Project Setup
- Project structure
- Virtual environment
- Git & GitHub integration
- Requirements management

### ✅ Phase 02 - Data Ingestion & Validation
- Configuration management
- Custom logging
- Exception handling
- Utility functions
- Data ingestion pipeline
- Schema-based data validation

### ⏳ Upcoming
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- MLflow
- FastAPI
- Docker
- Cloud Deployment

## Project Structure

```text
customer-churn-prediction/
│
├── app/
├── configs/
│   ├── config.yaml
│   └── schema.yaml
│
├── data/
│   ├── Raw/
│   ├── Interim/
│   └── Processed/
│
├── logs/
├── models/
├── notebooks/
├── scripts/
│
├── src/
│   ├── config.py
│   ├── logger.py
│   ├── exception.py
│   ├── utils.py
│   ├── ingestion.py
│   ├── validation.py
│   └── __init__.py
│
├── tests/
├── main.py
├── requirements.txt
└── README.md
```

## ✅ Features Implemented

### Configuration Management
- YAML-based configuration
- Centralized project settings

### Logging
- Console logging
- Timestamped log files
- File & line number tracking

### Exception Handling
- Custom exception class
- Detailed error reporting

### Utility Module
- Directory creation
- CSV read/write helpers
- YAML reader

### Data Ingestion
- Reads dataset from configurable path
- Logging integrated
- Exception handling

### Data Validation
- Schema-based validation
- Required column verification
- Validation status reporting