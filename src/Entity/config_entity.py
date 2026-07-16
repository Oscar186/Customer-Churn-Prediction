from dataclasses import dataclass
from pathlib import Path


# ==============================
# Data Ingestion
# ==============================

@dataclass
class DataIngestionConfig:

    root_dir: Path

    source_data_path: Path

    local_data_file: Path

# ==============================
# Data Validation
# ==============================

@dataclass
class DataValidationConfig:

    root_dir: Path

    data_path: Path

    schema_path: Path

# ==============================
# Data Transformation
# ==============================

@dataclass
class DataTransformationConfig:

    root_dir: Path

    data_path: Path

    preprocessor_path: Path

    train_array_path: Path
    test_array_path: Path

# ==============================
# Model Trainer
# ==============================

@dataclass
class ModelTrainerConfig:

    root_dir: Path

    train_array_path: Path

    test_array_path: Path

    trained_model_path: Path

    metrics_file_path: Path

    model_report_path: Path