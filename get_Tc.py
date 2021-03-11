from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error 

import warnings 
warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', category=DeprecationWarning)

import numpy as np
import pandas as pd


### Load trained Random Forest Regressor model
import zipfile
import os
import joblib

def load_model(offline_debug):
    global model,elems_x,elems_b,elems
    if offline_debug:
        model = joblib.load("../../sc_data_inc/for_the_app/Tc_model_8elem.pkl")
    else:
        with zipfile.ZipFile("model_8elem.zip") as zipref:
            zipref.extract("Tc_model_8elem.pkl")
        model = joblib.load("Tc_model_8elem.pkl")
        os.remove("Tc_model_8elem.pkl")

    elem_df = pd.read_csv("elem_df.csv")
    elems = elem_df["Symbol"].tolist()[::-1]
    elems_x = [el+"_x" for el in elems]
    elems_b = [el+"_b" for el in elems]
    # elems_atomic = {el[0]:el[1] for el in zip(elems,elem_df["Atomic number"].tolist()[::-1])}
    # elems_mass = {el[0]:el[1] for el in zip(elems,elem_df["Atomic weight (u)"].tolist()[::-1])}
    # elems_group = {el[0]:el[1] for el in zip(elems,elem_df["Group"].tolist()[::-1])}
    # elems_period = {el[0]:el[1] for el in zip(elems,elem_df["Period"].tolist()[::-1])}


#### After manually composing compound Get critical temperature.

vcComp = []
Comp = []
vcTc = 0
Tc = 0
def geTc(dict_new):
    global Tc,Comp,vcTc,vcComp,elems_x,elems_b,elems
    
    test_X = pd.DataFrame(columns=elems_x)
    
    col_prop = list(filter(lambda x: dict_new[x[:-2]]>0, elems_x))
    col_vrop = list(map(lambda x: dict_new[x[:-2]], col_prop))
    col_sum = sum(col_vrop)
    col_vrop = list(map(lambda x: x/col_sum, col_vrop))
    col_fluc = np.meshgrid(*[[0,-xyz/10,(1-xyz)/10] for xyz in col_vrop])
    col_delp = list(zip(*[c_.flatten() for c_ in col_fluc]))
    col_diff = np.array(col_vrop)[None,:] + col_delp
    col_diff /= np.sum(col_diff,axis=1,keepdims=True)
    col_diff = np.unique(col_diff,axis=0)
    test_X[col_prop] = pd.DataFrame(col_diff,columns=col_prop)

    
    Y_pred = model.predict(test_X.loc[:,elems_x])
    best_compos = np.argmax(Y_pred)
    Tc = Y_pred[0]
    vcTc = Y_pred[best_compos]
    Comp = [(x[:-2],y) for x,y in zip(col_prop,col_vrop)]
    vcComp = [(x[:-2],y) for x,y in zip(col_prop,col_diff[best_compos])]
    
    return Tc,Comp,vcTc,vcComp


def preTc():
    return Tc,Comp,vcTc,vcComp


