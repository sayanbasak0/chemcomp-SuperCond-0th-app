from flask import Flask,render_template,request,url_for,redirect
from bokeh.models.annotations import Title
from bokeh.plotting import figure,show
import numpy as np
from bokeh.embed import file_html,components
from bokeh.resources import CDN
import sys
# import elements
import src.element_ct_cc as element_ct_cc
import src.element_cc_ct as element_cc_ct
### Load trained Random Forest Regressor model
from src.const_trans import constituent_transformer # required to load scikit-learn pipeline with customized transformer
import joblib
from src.plot_compos import composition_8elem
from src.get_Tc import temperature_8elem

mylink = "/"
HEADING = "Searching for chemical compositions of Superconductors"

app = Flask(__name__, static_url_path='/static' )

@app.route('/crit_temp',methods = ['POST','GET'])
def crit_temp():
    print(request.method)
    print(request.form.get('redirect'))
    if request.method == 'POST':
        sess_key = request.form.get('SESS_KEY')
        if request.form.get("Update Plot"):
            defaultab = "Prediction-Tab"
        elif request.form.get("Critical Temperature redirect"):
            defaultab = "Prediction-Tab"
        else:
            defaultab = "Method-Tab"
    if request.method == 'GET':
        sess_key = f"{np.random.randint(0,999999):08d}"
        defaultab = "Periodic-Tab"

    modelTc = joblib.load("src/data/Tc_model_8elem.pkl")
    get_Temperature = temperature_8elem(modelTc)
    parse_elements = element_cc_ct.elements_parser(random_session=sess_key)
    
    p_table,pong_table,selems,defaultab,no_of_elems,prop_of_elems = parse_elements.update_composition(request.form)
    Tc,comp_list,altTc,altcomp_list = get_Temperature.geTc(selems)
    return render_template('crit_temp.html', 
                            p_table=p_table, 
                            pong_table=pong_table, 
                            selems=selems,
                            pelems=selems,
                            Tc=Tc,
                            comp_list=comp_list,
                            altTc=altTc,
                            altcomp_list=altcomp_list,
                            head1=HEADING, 
                            defaultab=defaultab,
                            no_of_elems=no_of_elems,
                            prop_of_elems=prop_of_elems,
                            custom_link=mylink,
                            sess_key=sess_key)


@app.route('/chem_comp',methods = ['POST','GET'])
def chem_comp():
    print(request.method)
    print(request.form.get('redirect'))
    if request.method == 'POST':
        sess_key = request.form.get('SESS_KEY')
        if request.form.get("Update Plot"):
            defaultab = "Prediction-Tab"
        else:
            defaultab = "Method-Tab"
    if request.method == 'GET':
        sess_key = f"{np.random.randint(0,999999):08d}"
        defaultab = "Periodic-Tab"
    
    modelCompos = joblib.load("src/data/composTc_model_8elem.pkl")
    plot_Composition = composition_8elem(modelCompos)
    parse_elements = element_ct_cc.elements_parser(random_session=sess_key)

    p_table,pong_table,selems,defaultab,no_of_elems = parse_elements.update_elements(request.form)
    plot_script,plot_div,pelems,maxTc,comp_list = plot_Composition.update_plot(selems)
    return render_template('chem_comp.html', 
                            p_table=p_table, 
                            pong_table=pong_table, 
                            selems=selems,
                            pelems=pelems,
                            maxTc=maxTc,
                            comp_list=comp_list,
                            head1=HEADING, 
                            plot_div=plot_div, 
                            plot_script=plot_script, 
                            defaultab=defaultab,
                            no_of_elems=no_of_elems,
                            custom_link=mylink,
                            sess_key=sess_key)


@app.route('/about',methods = ['POST','GET'])
def about():
    print(request.method)
    print(request.form.get('redirect'))
    if request.method == 'POST':
        sess_key = request.form.get('SESS_KEY')
    if request.method == 'GET':
        sess_key = f"{np.random.randint(0,999999):08d}"
    return render_template('about.html', 
                            head1=HEADING,
                            custom_link=mylink,
                            sess_key=sess_key
                            )

@app.route('/',methods = ['POST', 'GET'])
def index():
    print(request.method)
    print(request.form.get('redirect'))
    if request.method == 'POST':
        sess_key = request.form.get('SESS_KEY')
        if request.form.get('redirect') in ['chem_comp','crit_temp','about'] :
            return redirect(url_for(request.form.get('redirect')), code=307)
    if request.method == 'GET':
        sess_key = f"{np.random.randint(0,999999):08d}"

    return render_template('index.html', 
                            head1=HEADING,
                            custom_link=mylink,
                            sess_key=sess_key
                            )

import glob
import os
import time
if __name__== '__main__':
    # cleaning old files
    files = glob.glob("src/data/temp/elements_sess?_*.pkl")
    fileSessKeys = []
    for file in files:
        currentTime = time.time()
        fileSessKey = file.split("_")[2].split(".")[0] 
        fileModTimes = []
        for i in range(1,3,1):
            try:
                fileModTime = os.path.getmtime(f"elements_sess{i}_{fileSessKey}.pkl")
                fileModTimes.append(fileModTime)
            except FileNotFoundError:
                pass
        if fileModTimes:
            fileModTime = max(fileModTimes)
            if (currentTime-fileModTime>600):
                print(f"Deleting Stale Files: elements_sess?_{fileSessKey}.pkl - Last Modified: {(currentTime-fileModTime)/3600:.2f} hrs ago")
                for i in range(1,3,1):
                    try:
                        os.remove(f"elements_sess{i}_{fileSessKey}.pkl")
                    except FileNotFoundError:
                        pass
            else:
                fileSessKeys.append(fileSessKey)
    
    # parse_elements = elements.elements_parser(make_file=True, random_session=RANDOM_SESS_KEY)
    # plot_Composition = plot_compos.composition_8elem()
    # get_Temperature = get_Tc.temperature_8elem()

    # app.run(port=8000, debug=True)
    app.run(port=33507)

