from dataclasses import dataclass
from pathlib import Path


# ==========================
# Data Ingestion
# ==========================

@dataclass
class DataIngestionArtifact:

    raw_data_path: Path


# ==========================
# Data Validation
# ==========================

@dataclass
class DataValidationArtifact:
    validation_status: bool
    validated_data_path: Path


# ==========================
# Data Transformation
# ==========================

@dataclass
class DataTransformationArtifact:

    train_array_path: Path

    test_array_path: Path

    preprocessor_path: Path

    # trained_model_path: str

    # metrics_path: str

    # report_path: str


# ==========================
# Model Trainer
# ==========================

@dataclass
class ModelTrainerArtifact:

    trained_model_path: Path

    metrics_file_path: Path

    report_file_path: Path

    best_model_name: str

    best_score: float

    # train_score: float

    # test_score: float