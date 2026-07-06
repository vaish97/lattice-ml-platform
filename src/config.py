"""
Configuration file for the project.

All configurable parameters should be stored here.
"""

from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

TRAIN_DATA = RAW_DATA_DIR / "TrainDataStudy1.csv"

# Models
MODEL_DIR = PROJECT_ROOT / "models"

# Figures
FIGURE_DIR = PROJECT_ROOT / "docs" / "figures"

# Random seed
RANDOM_STATE = 42

# Dataset split
TEST_SIZE = 0.20
