"""
"""
Utility functions used across the project.
"""

from pathlib import Path
import joblib


def create_directory(directory):
    """
    Create directory if it does not exist.
    """
    Path(directory).mkdir(
        parents=True,
        exist_ok=True,
    )


def save_model(model, file_path):
    """
    Save trained model.
    """
    joblib.dump(model, file_path)


def load_model(file_path):
    """
    Load trained model.
    """
    return joblib.load(file_path)
