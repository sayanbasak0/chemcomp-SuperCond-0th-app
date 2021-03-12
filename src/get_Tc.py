from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error 
# from .const_trans import constituent_transformer # required to load scikit-learn pipeline with customized transformer
# import warnings 
# warnings.filterwarnings('ignore')
# warnings.filterwarnings('ignore', category=DeprecationWarning)

import numpy as np
import pandas as pd

### Load trained Random Forest Regressor model
import joblib
import os
module_path = os.path.split(__file__)[0]

#### After manually composing compound Get critical temperature.

class temperature_8elem:
    def __init__(self, model):
        # load model and define global as class variables
        self.model = model
        # self.model = joblib.load("Tc_model_8elem.pkl")
        self.elem_df = pd.read_csv(os.path.join(module_path,"data/elem_df.csv"))
        self.elems = self.elem_df["Symbol"].tolist()[::-1]
        self.elems_x = [el+"_x" for el in self.elems]
        self.elems_b = [el+"_b" for el in self.elems]
        # self.elems_atomic = {el[0]:el[1] for el in zip(self.elems,self.elem_df["Atomic number"].tolist()[::-1])}
        # self.elems_mass = {el[0]:el[1] for el in zip(self.elems,self.elem_df["Atomic weight (u)"].tolist()[::-1])}
        # self.elems_group = {el[0]:el[1] for el in zip(self.elems,self.elem_df["Group"].tolist()[::-1])}
        # self.elems_period = {el[0]:el[1] for el in zip(self.elems,self.elem_df["Period"].tolist()[::-1])}
        self.vcComp = []
        self.Comp = []
        self.vcTc = 0
        self.Tc = 0
        
    def geTc(self,dict_new):
        
        test_X = pd.DataFrame(columns=self.elems_x)
        
        col_prop = list(filter(lambda x: dict_new[x[:-2]]>0, self.elems_x))
        col_vrop = list(map(lambda x: dict_new[x[:-2]], col_prop))
        col_sum = sum(col_vrop)
        col_vrop = list(map(lambda x: x/col_sum, col_vrop))
        col_fluc = np.meshgrid(*[[0,-xyz/10,(1-xyz)/10] for xyz in col_vrop])
        col_delp = list(zip(*[c_.flatten() for c_ in col_fluc]))
        col_diff = np.array(col_vrop)[None,:] + col_delp
        col_diff /= np.sum(col_diff,axis=1,keepdims=True)
        col_diff = np.unique(col_diff,axis=0)
        test_X[col_prop] = pd.DataFrame(col_diff,columns=col_prop)

        
        Y_pred = self.model.predict(test_X.loc[:,self.elems_x])
        best_index = np.argmax(Y_pred)
        self.Tc = Y_pred[0]
        self.vcTc = Y_pred[best_index]
        self.Comp = [(x[:-2],y) for x,y in zip(col_prop,col_vrop)]
        self.vcComp = [(x[:-2],y) for x,y in zip(col_prop,col_diff[best_index])]
        
        return self.Tc,self.Comp,self.vcTc,self.vcComp


    def preTc(self):
        return self.Tc,self.Comp,self.vcTc,self.vcComp


