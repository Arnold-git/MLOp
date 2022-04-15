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


class MeanImputer(BaseEstimator, TransformerMixin):

  "Numerical missing value imputer"

  def __init__(self, variables):
    if not isinstance(variables, list):
      raise ValueError('Variable should be a list')
    self.variables = variables

  def fit(self, X, y=None):
    # put mean value for each variable in dictionary
    self.imputer_dict_ = X[self.variables].mean().to_dict()
    return self
  def transform(self, X):
    X = X.copy()
    for feature in self.variables:
      X[feature].fillna(self.imputer_dict_[feature],
                                                inplace=True)


    return X


class RareLabelCategoricalEncoder(BaseEstimator, TransformerMixin):

  """Group infrequent categories into a single string"""

  def __init__(self,  variables, tol=0.05):
    # specific default arguement before non-default arguement

    if not isinstance(variables, list):
      raise ValueError('variables should be a list')
    if not isinstance(tol, float):
      raise ValueError('tol should be a float')

    self.variables = variables
    self.tol = tol
  
  def fit(self, X, y=None):

    self.encoder_dict_ = {}

    for var in self.variables:

      t = pd.Series(X[var].value_counts(normalize=True))

      self.encoder_dict_[var] = list(t[t >= self.tol].index)

    return self

  def transform(self, X):
    X = X.copy()
    for feature in self.variables:
      X[feature] = np.where(
        X[feature].isin(self.encoder_dict_[feature]), X[feature], 'Rare')

    return X

class CategoricaEncoder(BaseEstimator, TransformerMixin):

  def __init__(self, variables):

    if not isinstance(variables, list):
      raise ValueError('variables should be a list')

    self.variables = variables

  def fir(self, X, y):
    temp = pd.concat([X, y], axis = 1)
    temp.columns = list(X.columns) + ['target']

    self.encoder_dict_ = {}

    for var in self.variables:
      t = temp.groupby([var])['target'].mean().sort_values(ascending=True).index
      self.encoder_dict_[var] = {k:1 for i, k in enumerate(t, 0)}


    return self

  def transform(self, X):

    X = X.copy()
    for feature in self.variables:
      X[feature] = X[feature].map(self.encoder_dict_[feature])

      return X