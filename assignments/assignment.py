import numpy as np
import pandas as pd


# TODO: Implement the Perceptron class
# This class will be evaluated based on GitHub classroom autograding
class Perceptron:
    """
    Implements a Perceptron classifier.

    Parameters
    ----------
    eta : float
        Specifies the learning rate (between 0.0 and 1.0).
    n_iter : int
        Defines the passes over the training dataset.
    random_state : int
        Sets the seed for the random number generator used for random weight initialization.

    Attributes
    ----------
    w_ : 1d-array
        Holds the weights after fitting.
    b_ : Scalar
        Contains the bias unit after fitting.
    errors_ : list
        Records the number of misclassifications (updates) in each epoch.

    """

    def __init__(self, eta: float = 0.01, n_iter: int = 50, random_state: int = 1):
        pass

    def fit(self, X: np.ndarray, y: np.ndarray):
        """
        Fits the training data.

        Parameters
        ----------
        X : {array-like}, shape = [n_examples, n_features]
            Training vectors, where n_examples is the number of examples and
            n_features is the number of features.
        y : array-like, shape = [n_examples]
            Target values.

        Returns
        -------
        self : object

        """
        pass

    def predict(self, X: np.ndarray):
        """Returns the class label after the unit step."""
        pass


# TODO: Implement the function to load the penguin data.
def load_penguin_data(self):
    """
    Load the penguin dataset from the provided URL (see below) and return it as a pandas dataframe.
    The dataframe will only include the following columns:
    - species
    - bill_length_mm
    - bill_depth_mm

    The data can be loaded from the following URL:
    "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/c19a904462482430170bfe2c718775ddb7dbb885/inst/extdata/penguins.csv"

    Returns
    -------
    pandas.DataFrame
        The loaded penguin dataset with only the specified columns.
    """
    url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/c19a904462482430170bfe2c718775ddb7dbb885/inst/extdata/penguins.csv"

    pass
