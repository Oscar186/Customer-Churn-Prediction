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


# ==========================
# Model Trainer
# ==========================

@dataclass
class ModelTrainerArtifact:

    trained_model_path: Path

    train_score: float

    test_score: float