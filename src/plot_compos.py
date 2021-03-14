# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error 
from .const_trans import constituent_transformer # required to load scikit-learn pipeline with customized transformer
# from sklearn.pipeline import Pipeline
# import warnings 
# warnings.filterwarnings('ignore')
# warnings.filterwarnings('ignore', category=DeprecationWarning)

import numpy as np
import pandas as pd

#### After manually selecting elements update plot.
from bokeh.plotting import figure
# from bokeh.embed import file_html
from bokeh.embed import components
# from bokeh.models import Label
from bokeh.models import Legend,HoverTool,ColumnDataSource
from bokeh.colors import HSL
# from memory_profiler import profile
# import dill
import joblib
import os
import gc
module_path = os.path.split(__file__)[0]

class composition_8elem:
    def __init__(self):
        pass
        
    def my_colors(self,ii,nn):
        return HSL(360*(ii+1)/nn,1,0.4).to_rgb().to_hex()
    # @profile
    def update_plot(self,dict_new):
        elem_df = pd.read_csv(os.path.join(module_path,"data","elem_df.csv"), usecols=["Symbol", "Element", "Atomic weight (u)", "Period", "Group"])
        self_elems = elem_df["Symbol"].tolist()[::-1]
        # self_elems_x = [el+"_x" for el in self_elems]
        self_elems_b = [el+"_b" for el in self_elems]
        elems_mass = {el[0]:el[1] for el in zip(self_elems, elem_df["Atomic weight (u)"].tolist()[::-1])}
        elem_group = {el[0]:el[1] for el in zip(self_elems, elem_df["Group"].tolist()[::-1])}
        elem_period = {el[0]:el[1] for el in zip(self_elems, elem_df["Period"].tolist()[::-1])}
        self_elements = {el[0]:el[1] for el in zip(self_elems, elem_df["Element"].tolist()[::-1])}
        del(elem_df)
        gc.collect()
        trans = constituent_transformer(
            col_names=self_elems,
            sort_by=[elem_period, elem_group, elems_mass],
            ext="_b",
            stdScale=["Critical Temperature"]
        )
        del(elems_mass,elem_group,elem_period)
        gc.collect()
        temp_df = pd.read_csv(os.path.join(module_path,"data","data_df.csv"), usecols=["Critical Temperature"])
        trans.fit(temp_df.loc[:,["Critical Temperature"]])
        del(temp_df)
        gc.collect()
        
        t_lim = [0,200]
        col_bool = list(filter(lambda x: dict_new[x[:-2]]>0, self_elems_b))
        col_vool = list(map(lambda x: dict_new[x[:-2]], col_bool))
        test_X = pd.DataFrame(columns=col_bool+["Critical Temperature"])
        test_X["Critical Temperature"] = np.linspace(t_lim[0],t_lim[1],t_lim[1]+1)
        test_X.loc[:, col_bool] = col_vool
        col_out = list(filter(lambda x: dict_new[x]>0, self_elems))
        test_X.fillna(0, inplace=True)
        
        tran_X = trans.static_transformer(
                X=test_X.loc[:,col_bool+["Critical Temperature"]],
                cols=col_out
            )
        del(trans)
        gc.collect()
        model = joblib.load(os.path.join(module_path,"data","composTc_rfrPipe_8elem_nest50_md40.pkl"))
        # with open(os.path.join(module_path,'data','predict_composTc_rfrPipe_8elem_new.pkl'), 'rb') as f:
        #     model_predict = dill.load(f)
        pred_df = pd.DataFrame(
            model.predict(
                tran_X
            )[:,:len(col_out)], 
            columns=col_out
        )
        del(model,tran_X)
        gc.collect()
        line_types = ["dashed","solid"]
        elem_present = pred_df.loc[:,((pred_df[col_out]*test_X[col_bool].values).sum(axis=0)>0)].columns
        elem_present = list(zip(elem_present, 
                                map(lambda x: line_types[1], range(len(elem_present))),
                                map(lambda x: pred_df.iloc[-1,pred_df.columns.get_loc(x)], elem_present)
                            )
                        )
        elem_absent = []
        pred_df["Critical Temperature"] = test_X["Critical Temperature"]
        del(test_X)
        gc.collect()
        elems_list = sorted(elem_present+elem_absent,key=lambda wxyz: (-wxyz[2]))
        elem_list,dash_list,prop_list = list(zip(*elems_list))
        elem_list = list(elem_list)
        dash_list = list(dash_list)
        prop_list = list(prop_list)
        color_list = list(map(self.my_colors, range(len(elems_list)), [len(elems_list)]*len(elems_list)))
        
        maxTc_indx = 0
        for i in range(len(pred_df)-1,0,-1):
            if any(pred_df.loc[i,elem_list]!=pred_df.loc[i-1,elem_list]):
                maxTc_indx = i
                break
        self_maxTc = pred_df.loc[maxTc_indx,"Critical Temperature"]
        self_elem_prop = {elem:pred_df.loc[maxTc_indx,elem]*100 if elem in pred_df.columns else 0 for elem,pres in dict_new.items() }
        self_elem_prop.update({em:0 for em in ["space","arrow","Ln","An"]})
        self_compos = [(sym,x) for sym,x in zip(elem_list,prop_list) if x>0]
        legend_it = []
        source = ColumnDataSource({'x': np.array([self_maxTc]*len(elem_list)), 
                                    'y': np.array(100*pred_df.loc[self_maxTc,elem_list]), 
                                    'series_name': np.array(elem_list), 
                                    'prop_maxTc': np.array(100*pred_df.loc[self_maxTc,elem_list]),
                                    'element_name': np.array(list(map(lambda x: self_elements[x], elem_list)))
                                    })
                                    
        self_pfig = figure(width=1200, height=540, x_range=(0, 150))
        
        mfig = self_pfig.circle('x', 'y', source=source, color='#000000', line_alpha=0.2, fill_alpha=0, radius=0.5, line_width=2, hover_line_alpha=1.0)
        mfig = self_pfig.line('x', 'y', source=source, color='#000000', hover_line_width=2)
        legendttl = f"Composition at Max($T_c$) = {self_maxTc:.0f}K"
        legend_it.append((legendttl, [mfig]))
    
        for elem,lash,colr,prop in zip(elem_list,dash_list,color_list,prop_list):
            legendsym = f"{elem} ~ {(prop*100):.2f}%"
            source = ColumnDataSource({'x': np.array(pred_df["Critical Temperature"].values), 
                                        'y': np.array(100*pred_df[elem].values), 
                                        'series_name': np.array([elem]*len(pred_df)), 
                                        'prop_maxTc': np.array([prop*100]*len(pred_df)),
                                        'element_name': np.array([self_elements[elem]]*len(pred_df))
                                        })
            # cfig = self_pfig.scatter('x', 'y', 
            #                 source=source,
            #                 fill_alpha=0.0, 
            #                 line_alpha=0.2, 
            #                 line_width=1,
            #                 line_color=colr,
            #                 hover_line_alpha=1.0, 
            #                 hover_line_color=colr,
            #                 hover_line_width=1
            #                 )
            lfig = self_pfig.line('x', 'y', 
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
            
        self_pfig.add_tools(HoverTool(show_arrow=False, 
                                line_policy='nearest', 
                                tooltips=[("Element", "@element_name"), 
                                            ("Symbol", "@series_name"), 
                                            ("Proportion", "@y{0.00}%"), 
                                            (f"At Max(T_c)={self_maxTc:.0f}K", "@prop_maxTc{0.00}%")
                                        ]
                                )
                    )
        if len(elems_list)>0:
            # self_pfig.legend.title = "Composition at Max($T_c$)"
            legend = Legend(items=legend_it)
            legend.click_policy="hide"
            # legend.title = f"Composition at Max($T_c$) = {maxTc}"
            self_pfig.add_layout(legend, 'right')
            self_pfig.legend.label_text_font_size = '12pt'
        self_pfig.xaxis.axis_label = "Critical Temperature (T<sub>c</sub>) [K]"
        self_pfig.yaxis.axis_label = "Predicted proportion of elements [%]"
        self_pfig.xaxis.axis_label_text_font_size = "16pt"
        self_pfig.yaxis.axis_label_text_font_size = "16pt"
        
        self_plot_script,self_plot_div = components(self_pfig)
        
        return self_plot_script,self_plot_div,self_elem_prop,self_maxTc,self_compos
