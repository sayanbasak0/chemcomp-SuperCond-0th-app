# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error 
from .const_trans import constituent_transformer # required to load scikit-learn pipeline with customized transformer
# import warnings 
# warnings.filterwarnings('ignore')
# warnings.filterwarnings('ignore', category=DeprecationWarning)

import numpy as np
import pandas as pd

# from memory_profiler import profile
import joblib
# import dill
import os
import gc
module_path = os.path.split(__file__)[0]

#### After manually composing compound Get critical temperature.

class temperature_8elem:
    def __init__(self):
        pass
    # @profile
    def scanTc(self,dict_new):
        
        elem_df = pd.read_csv(os.path.join(module_path,"data","elem_df.csv"), usecols=["Symbol","Atomic weight (u)", "Period", "Group"])
        self_elems = elem_df["Symbol"].tolist()[::-1]
        self_elems_x = [el+"_x" for el in self_elems]
        # self_elems_b = [el+"_b" for el in self_elems]
        
        elems_mass = {el[0]:el[1] for el in zip(self_elems,elem_df["Atomic weight (u)"].tolist()[::-1])}
        elem_group = {el[0]:el[1] for el in zip(self_elems,elem_df["Group"].tolist()[::-1])}
        elem_period = {el[0]:el[1] for el in zip(self_elems,elem_df["Period"].tolist()[::-1])}
        del(elem_df)
        gc.collect()
        trans = constituent_transformer(
            col_names=self_elems,
            sort_by=[elem_period, elem_group, elems_mass],
            ext="_x"
        )
        del(elem_group,elem_period,elems_mass)
        gc.collect()
        col_elems = list(filter(lambda x: dict_new[x]>0, self_elems))
        col_prop = list(filter(lambda x: dict_new[x[:-2]]>0, self_elems_x))
        col_vrop = list(map(lambda x: dict_new[x[:-2]], col_prop))
        col_sum = sum(col_vrop)
        col_vrop = list(map(lambda x: x/col_sum, col_vrop))
        col_fluc = np.meshgrid(*[[0,-xyz/10,(1-xyz)/10] for xyz in col_vrop])
        col_delp = list(zip(*[c_.flatten() for c_ in col_fluc]))
        col_diff = np.array(col_vrop)[None,:] + col_delp
        col_diff /= np.sum(col_diff,axis=1,keepdims=True)
        # col_diff = np.unique(col_diff,axis=0)
        del(col_delp,col_fluc)
        gc.collect()
        test_X = pd.DataFrame(columns=col_prop)
        test_X[col_prop] = pd.DataFrame(col_diff,columns=col_prop)
        test_X.fillna(0, inplace=True)
        tran_X = trans.static_transformer(
            X=test_X.loc[:,col_prop],
            cols=col_elems
        )
        del(trans,test_X)
        gc.collect()
        model = joblib.load(os.path.join(module_path,"data","Tc_rfrPipe_8elem_nest50_md40.pkl"))
        # with open(os.path.join(module_path,'data','predict_Tc_rfrPipe_8elem.pkl'), 'rb') as f:
        #     model_predict = dill.load(f)
        Y_pred = model.predict(
            tran_X
        )
        del(model,tran_X)
        gc.collect()
        best_index = np.argmax(Y_pred)
        # org_index = np.argmax(col_vrop=)
        self_Tc = Y_pred[0]
        self_vcTc = Y_pred[best_index]
        del(Y_pred)
        gc.collect()
        self_Comp = [(x[:-2],y) for x,y in zip(col_prop,col_vrop)]
        self_vcComp = [(x[:-2],y) for x,y in zip(col_prop,col_diff[best_index])]
        del(col_diff)
        gc.collect()
        self_elem_dict = {elem:pres*100 for elem,pres in dict_new.items() }
        self_elem_dict.update({em:0 for em in ["space","arrow","Ln","An"]})
        # print(self_Tc,self_Comp,self_vcTc,self_vcComp)
        return self_Tc,self_Comp,self_vcTc,self_vcComp,self_elem_dict

    def geTc(self,dict_new):
        
        elem_df = pd.read_csv(os.path.join(module_path,"data","elem_df.csv"), usecols=["Symbol","Atomic weight (u)", "Period", "Group"])
        self_elems = elem_df["Symbol"].tolist()[::-1]
        self_elems_x = [el+"_x" for el in self_elems]
        # self_elems_b = [el+"_b" for el in self_elems]
        
        elems_mass = {el[0]:el[1] for el in zip(self_elems,elem_df["Atomic weight (u)"].tolist()[::-1])}
        elem_group = {el[0]:el[1] for el in zip(self_elems,elem_df["Group"].tolist()[::-1])}
        elem_period = {el[0]:el[1] for el in zip(self_elems,elem_df["Period"].tolist()[::-1])}
        del(elem_df)
        gc.collect()
        trans = constituent_transformer(
            col_names=self_elems,
            sort_by=[elem_period, elem_group, elems_mass],
            ext="_x"
        )
        del(elem_group,elem_period,elems_mass)
        gc.collect()
        col_elems = list(filter(lambda x: dict_new[x]>0, self_elems))
        col_prop = list(filter(lambda x: dict_new[x[:-2]]>0, self_elems_x))
        col_vrop = list(map(lambda x: dict_new[x[:-2]], col_prop))
        col_sum = sum(col_vrop)
        col_vrop = list(map(lambda x: x/col_sum, col_vrop))
        
        col_diff = np.array([col_vrop])
        
        gc.collect()
        test_X = pd.DataFrame(columns=col_prop)
        test_X[col_prop] = pd.DataFrame(col_diff,columns=col_prop)
        test_X.fillna(0, inplace=True)
        tran_X = trans.static_transformer(
            X=test_X.loc[:,col_prop],
            cols=col_elems
        )
        del(trans,test_X)
        gc.collect()
        model = joblib.load(os.path.join(module_path,"data","Tc_rfrPipe_8elem_nest50_md40.pkl"))
        # with open(os.path.join(module_path,'data','predict_Tc_rfrPipe_8elem.pkl'), 'rb') as f:
        #     model_predict = dill.load(f)
        Y_pred = model.predict(
            tran_X
        )
        del(model,tran_X)
        gc.collect()
        
        self_Tc = Y_pred[0]
        
        del(Y_pred)
        gc.collect()
        self_Comp = [(x[:-2],y) for x,y in zip(col_prop,col_vrop)]
        
        del(col_diff)
        gc.collect()
        
        # print(self_Tc,self_Comp)
        return self_Tc,self_Comp
