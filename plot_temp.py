from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error 

import warnings 
warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', category=DeprecationWarning)

import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sb
import random

import matplotlib as mpl
mpl.rcParams['figure.facecolor'] = '#222222'
mpl.rcParams['axes.facecolor'] = '#222222'
mpl.rcParams['axes.labelcolor'] = '#edece9'
mpl.rcParams['xtick.color'] = '#edece9'
mpl.rcParams['ytick.color'] = '#edece9'
mpl.rcParams['text.color'] = '#edece9' 

### Load trained Random Forest Regressor model
import zipfile
import os
import pickle

def load_model(offline_debug):
    global model
    filebase = "rf_regressor"
    if offline_debug:
        with open("../../sc_data_inc/"+filebase+".dat", 'rb') as f:
            model = pickle.load(f)
    else:
        with zipfile.ZipFile(filebase+".zip") as zipref:
            zipref.extractall()

        with open(filebase+".dat", 'rb') as f:
            model = pickle.load(f)

        os.remove(filebase+".dat")

### Initialize input features 

data_head = pd.read_csv("SC_data_frac.csv",nrows=0) 
data_Tc = pd.read_csv("SC_data_frac.csv",usecols=["Critical Temperature"]) 

col_bool = [col[:-2]+"_bool" for col in data_head if col.endswith("_x")]

data_headr = ["Scaled T_c"]
data_headr.extend(col_bool)

data_Tc = data_Tc[data_Tc["Critical Temperature"]>0]
data_std = data_Tc.std()

#### After manually selecting elements update plot.
from bokeh.plotting import figure,show
from bokeh.embed import file_html,components
from bokeh.util.compiler import TypeScript
from bokeh.palettes import Turbo256
from bokeh.models import Label,Legend,HoverTool,ColumnDataSource
from bokeh.colors import HSL
from collections import defaultdict
def my_colors(ii,nn):
    return HSL(360*(ii+1)/nn,1,0.4).to_rgb().to_hex()

plot_div = ""
plot_script = ""
elem_prop = {}
compos = []
maxTc = 0
pfig = figure(width=1200, height=540, x_range=(0, 100))
def update_plot(dict_new):
    global plot_div,plot_script,pfig,elem_prop,maxTc,compos
    pfig = figure(width=1200, height=540, x_range=(0, 100))
    
    t_lim = [0,150]
    
    test_X = pd.DataFrame(columns=["Scaled T_c","dict_elem"])
    UnScaled_T_c = np.linspace(t_lim[0],t_lim[1],151)
    test_X["Scaled T_c"] = UnScaled_T_c/data_std["Critical Temperature"]
    col_out = list(map(lambda x: x[:-5], col_bool))
    dict_new_ = dict(map(lambda x: (x[0]+"_bool", x[1]), dict_new.items()))
    test_X.loc[:,"dict_elem"] = [dict_new_]*len(test_X)
    test_X = pd.concat([test_X.drop(["dict_elem"],axis=1),test_X["dict_elem"].apply(pd.Series)],axis=1)
    
    
    Y_pred = model.predict(test_X[data_headr])
    pred_df = pd.DataFrame(Y_pred,columns=col_out)
    # print(col_out,col_bool)
    line_types = ["dashed","solid"]
    elem_present = pred_df.loc[:,((pred_df[col_out]*test_X[col_bool].values).sum(axis=0)>0)].columns
    elem_present = list(zip(elem_present, 
                            map(lambda x: line_types[1], range(len(elem_present))),
                            map(lambda x: pred_df.iloc[-1,pred_df.columns.get_loc(x)], elem_present)
                           )
                       )
    elem_absent = pred_df.loc[:,((pred_df[col_out]*(1-test_X[col_bool].values)).sum(axis=0)>0)].columns
    elem_absent = list(zip(elem_absent, 
                           map(lambda x: line_types[0], range(len(elem_absent))),
                           map(lambda x: pred_df.iloc[-1,pred_df.columns.get_loc(x)], elem_absent)
                          )
                      )
    pred_df["Critical Temperature"] = UnScaled_T_c
    
    elems_list = sorted(elem_present+elem_absent,key=lambda wxyz: (-wxyz[2]))
    elem_list,dash_list,prop_list = list(zip(*elems_list))
    elem_list = list(elem_list)
    dash_list = list(dash_list)
    prop_list = list(prop_list)
    color_list = list(map(my_colors, range(len(elems_list)), [len(elems_list)]*len(elems_list)))
    
    maxTc_indx = 0
    for i in range(len(pred_df)-1,0,-1):
        if any(pred_df.loc[i,elem_list]!=pred_df.loc[i-1,elem_list]):
            maxTc_indx = i
            break
    maxTc = pred_df.loc[maxTc_indx,"Critical Temperature"]
    elem_prop = {elem:pred_df.loc[maxTc_indx,elem]*100 if elem in pred_df.columns else 0 for elem,pres in dict_new.items() }
    elem_prop.update({em:0 for em in ["space","arrow","Ln","An"]})
    compos = [(sym,x) for sym,x in zip(elem_list,prop_list) if x>0]
    legend_it = []
    source = ColumnDataSource({'x': [maxTc]*len(elem_list), 
                                'y': 100*pred_df.loc[maxTc,elem_list], 
                                'series_name': elem_list, 
                                'prop_maxTc': 100*pred_df.loc[maxTc,elem_list],
                                'excess': list(map(lambda x: x=="dashed", dash_list))
                                })
    mfig = pfig.circle('x', 'y', source=source, color='#000000', line_alpha=0.2, fill_alpha=0, radius=0.5, line_width=2, hover_line_alpha=1.0)
    mfig = pfig.line('x', 'y', source=source, color='#000000', hover_line_width=2)
    legendttl = f"Composition at Max($T_c$) = {maxTc:.0f}K"
    legend_it.append((legendttl, [mfig]))
   
    for elem,lash,colr,prop in zip(elem_list,dash_list,color_list,prop_list):
        legendsym = f"{elem} ~ {(prop*100):.2f}%"
        source = ColumnDataSource({'x': pred_df["Critical Temperature"].values, 
                                    'y': 100*pred_df[elem].values, 
                                    'series_name': [elem]*len(pred_df), 
                                    'prop_maxTc': [prop*100]*len(pred_df),
                                    'excess': [lash=="dashed"]*len(pred_df)
                                    })
        cfig = pfig.scatter('x', 'y', 
                        source=source,
                        fill_alpha=0.0, 
                        line_alpha=0.2, 
                        line_width=1,
                        line_color=colr,
                        hover_line_alpha=1.0, 
                        hover_line_color=colr,
                        hover_line_width=1
                        )
        lfig = pfig.line('x', 'y', 
                        source=source,
                        line_dash=lash, 
                        color=colr, 
                        alpha=0.8, 
                        line_width=2,
                        muted_color=colr, 
                        muted_alpha=0.2,
                        muted_line_width=1,
                        hover_line_alpha=1.0, 
                        hover_line_color=colr,
                        hover_line_width=3
                        )
        
        legend_it.append((legendsym, [lfig]))
        
    pfig.add_tools(HoverTool(show_arrow=False, 
                            line_policy='nearest', 
                            tooltips=[("Element", "@series_name"), 
                                        ("Proportion", "@y{0.00}%"), 
                                        (f"At Max(T_c)={maxTc:.0f}K", "@prop_maxTc{0.00}%"), 
                                        ("Not in Input", "@excess") 
                                    ]
                            )
                )
    if len(elems_list)>0:
        # pfig.legend.title = "Composition at Max($T_c$)"
        legend = Legend(items=legend_it)
        legend.click_policy="hide"
        # legend.title = f"Composition at Max($T_c$) = {maxTc}"
        pfig.add_layout(legend, 'right')
        pfig.legend.label_text_font_size = '12pt'
    pfig.xaxis.axis_label = "Critical Temperature ($T_c$) [K]"
    pfig.yaxis.axis_label = "Predicted proportion of elements [%]"
    pfig.xaxis.axis_label_text_font_size = "16pt"
    pfig.yaxis.axis_label_text_font_size = "16pt"
    
    plot_script,plot_div = components(pfig)
    return plot_script,plot_div,elem_prop,maxTc,compos


def old_plot():
    return plot_script,plot_div,elem_prop,maxTc,compos


