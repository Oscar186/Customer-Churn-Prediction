from dataclasses import dataclass
from pathlib import Path


# ==============================
# Data Ingestion
# ==============================

@dataclass(frozen=True)
class DataIngestionConfig:

    root_dir: Path

    source_url: str

    local_data_file: Path

# ==============================
# Data Validation
# ==============================

@dataclass(frozen=True)
class DataValidationConfig:

    root_dir: Path

    data_path: Path

    schema_path: Path

# ==============================
# Data Transformation
# ==============================

@dataclass(frozen=True)
class DataTransformationConfig:

    root_dir: Path

    data_path: Path

    preprocessor_path: Path

    train_array_path: Path
    test_array_path: Path

# ==============================
# Model Trainer
# ==============================

@dataclass(frozen=True)
class ModelTrainerConfig:

    root_dir: Path

    train_array_path: Path

    test_array_path: Path

    trained_model_path: Path