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
        model = joblib.load("../../sc_data_inc/for_the_app/composTc_model_8elem.pkl")
    else:
        with zipfile.ZipFile("model_8elem.zip") as zipref:
            zipref.extract("composTc_model_8elem.pkl")
        model = joblib.load("composTc_model_8elem.pkl")
        os.remove("composTc_model_8elem.pkl")

    elem_df = pd.read_csv("elem_df.csv")
    elems = elem_df["Symbol"].tolist()[::-1]
    elems_x = [el+"_x" for el in elems]
    elems_b = [el+"_b" for el in elems]
    # elems_atomic = {el[0]:el[1] for el in zip(elems,elem_df["Atomic number"].tolist()[::-1])}
    # elems_mass = {el[0]:el[1] for el in zip(elems,elem_df["Atomic weight (u)"].tolist()[::-1])}
    # elems_group = {el[0]:el[1] for el in zip(elems,elem_df["Group"].tolist()[::-1])}
    # elems_period = {el[0]:el[1] for el in zip(elems,elem_df["Period"].tolist()[::-1])}


#### After manually selecting elements update plot.
from bokeh.plotting import figure
from bokeh.embed import file_html,components
from bokeh.models import Label,Legend,HoverTool,ColumnDataSource
from bokeh.colors import HSL

def my_colors(ii,nn):
    return HSL(360*(ii+1)/nn,1,0.4).to_rgb().to_hex()

plot_div = ""
plot_script = ""
elem_prop = {}
compos = []
maxTc = 0
pfig = figure(width=1200, height=540, x_range=(0, 150))
def update_plot(dict_new):
    global plot_div,plot_script,pfig,elem_prop,maxTc,compos,elems_x,elems_b,elems
    pfig = figure(width=1200, height=540, x_range=(0, 150))
    
    t_lim = [0,200]
    
    test_X = pd.DataFrame(columns=elems_b+["Critical Temperature"])
    UnScaled_T_c = np.linspace(t_lim[0],t_lim[1],201)
    test_X["Critical Temperature"] = UnScaled_T_c
    col_bool = list(filter(lambda x: dict_new[x[:-2]]>0, elems_b))
    col_vool = list(map(lambda x: dict_new[x[:-2]], col_bool))
    test_X.loc[:, col_bool] = col_vool
    col_out = list(filter(lambda x: dict_new[x]>0, elems))
    
    Y_pred = model.predict(test_X.loc[:,elems_b+["Critical Temperature"]])
    pred_df = pd.DataFrame(Y_pred[:,:len(col_out)],columns=col_out)
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


