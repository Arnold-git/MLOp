import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin


class TemporalVariableTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, variables, reference_variable):

        if not isinstance(variables, list):
            raise ValueError('variable should be a list')

        self.variables = variables
        self.reference_variable = reference_variable

    def fit(self, X, y=None):

        return self

        # check
        # https://stackoverflow.com/questions/43380042/purpose-of-return-self-python

    def transform(self, X):

        X = X.copy()

        for feature in self.variables:
            X[feature] = X[self.reference_variable] -X[feature]
        return X



class Mapper(BaseEstimator, TransformerMixin):

  def __init__(self, variables, mappings):

    if not isinstance(variables, list):
      raise ValueError('variables should be a list')

    self.variables = variables
    self.mappings = mappings

  def fit(self, X, y = None):

    return self

  def transform(self, X):

    X = X.copy()

    for feature in self.variables:
      X[feature] = X[feature].map(self.mappings)

      return X