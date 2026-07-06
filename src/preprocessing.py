"""
"""
Data preprocessing functions.

This module contains functions for:
- Loading data
- Cleaning data
- Feature engineering
- Train-test split
"""

import pandas as pd


def load_data(file_path):
    """
    Load dataset.

    Parameters
    ----------
    file_path : str or Path

    Returns
    -------
    pandas.DataFrame
    """
    return pd.read_csv(file_path)


def preprocess_data(df):
    """
    Placeholder for preprocessing steps.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
    """
    return df


def split_features_target(df, target_column):
    """
    Separate features and target variable.
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]

    return X, y
