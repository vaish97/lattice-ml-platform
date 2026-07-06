"""
"""
Model training functions.

This module contains training functions for:
- MLP
- Gradient Boosting
- Gaussian Process Regression
"""

from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.gaussian_process import GaussianProcessRegressor


def train_mlp(X_train, y_train):
    """Train MLP model."""

    model = MLPRegressor()

    model.fit(X_train, y_train)

    return model


def train_gradient_boosting(X_train, y_train):
    """Train Gradient Boosting model."""

    model = GradientBoostingRegressor()

    model.fit(X_train, y_train)

    return model


def train_gaussian_process(X_train, y_train):
    """Train Gaussian Process model."""

    model = GaussianProcessRegressor()

    model.fit(X_train, y_train)

    return model
