from sklearn import base
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

### Constituent Transformer
class constituent_transformer(base.BaseEstimator, base.TransformerMixin):
    
    def __init__(self, col_names, sort_by, ext="", passthru=[], stdScale=[]):
        self.col_names = col_names  # We will need these in transform()
        self.sort_by = sort_by  # We will need these in transform()
        self.ext = ext  # We will need these in transform()
        self.passthru = passthru  # We will need these in transform()
        self.stdScale = stdScale  # We will need these in transform()
    
    def fit(self, X, y=None):
        self.col_sorted = sorted(self.col_names,key=lambda x: [-sb[x] for sb in self.sort_by])
        self.col_ext = [col+self.ext for col in self.col_sorted]
        if self.stdScale:
            self.ssc = StandardScaler()
            self.ssc.fit(X[self.stdScale])
        return self
    
    def row_transform(self,X):
        Y = []
        for Xrow in X.to_numpy():
            Yrow = [0 for _ in range(8*len(self.sort_by))]
            i=0
            for xi,Xitem in enumerate(Xrow):
                if Xitem>0:
                    for j in range(len(self.sort_by)):
                        Yrow[len(self.sort_by)*i+j] = self.sort_by[j][self.col_sorted[xi]]*Xitem
                    i += 1
            Y.append(Yrow)
        return pd.DataFrame(Y)
    
    def transform(self, X):
        # Return an array with the same number of rows as X and one
        # column for each in self.col_names
        Y = self.row_transform(X[self.col_ext])
        if self.passthru:
            Y[self.passthru] = X[self.passthru]
        if self.stdScale:
            Y[self.stdScale] = self.ssc.transform(X[self.stdScale])
        return Y
