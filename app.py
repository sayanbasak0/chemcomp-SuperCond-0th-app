from flask import Flask,render_template,request,url_for,redirect
from bokeh.models.annotations import Title
from bokeh.plotting import figure,show
import numpy as np
from bokeh.embed import file_html,components
from bokeh.resources import CDN
import sys
import elements
import plot_compos
import get_Tc
from const_trans import constituent_transformer # required to load scikit-learn pipeline with customized transformer

mylink = "/"
HEADING = "Searching for chemical compositions of Superconductors"
RANDOM_SESS_KEY = f"{np.random.randint(0,999999):08d}"

app = Flask(__name__, static_url_path='/static' )

@app.route('/about')
def about():
    print(request.method)
    print(request.form.get('redirect'))
    return render_template('about.html', 
                            head1=HEADING,
                            custom_link=mylink)

@app.route('/',methods = ['POST', 'GET'])
def index():
    print(request.method)
    print(request.form.get('redirect'))
    if request.method == 'POST':
        if request.form.get('redirect') in ['chem_comp','crit_temp','about'] :
            return redirect(url_for(request.form.get('redirect')))

    return render_template('index.html', 
                            head1=HEADING,
                            custom_link=mylink)

@app.route('/crit_temp',methods = ['POST', 'GET'])
def crit_temp():
    get_Temperature = get_Tc.temperature_8elem()
    parse_elements = elements.elements_parser(random_session=RANDOM_SESS_KEY)
    print(request.method)
    print(request.form.get('redirect'))
    print(request.form.get('Critical Temperature redirect'))
    if request.method == 'POST':
        p_table,pong_table,selems,defaultab,no_of_elems,prop_of_elems = parse_elements.update_composition(request.form)
        if request.form.get("Update Plot"):
            defaultab = "Prediction-Tab"
            Tc,comp_list,altTc,altcomp_list = get_Temperature.geTc(selems)
        elif request.form.get("Critical Temperature redirect"):
            defaultab = "Prediction-Tab"
            Tc,comp_list,altTc,altcomp_list = get_Temperature.geTc(selems)
        else:
            defaultab = "Method-Tab"
            Tc,comp_list,altTc,altcomp_list = get_Temperature.preTc()
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
                                custom_link=mylink)

    elif request.method == 'GET':
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
                                custom_link=mylink)

@app.route('/chem_comp',methods = ['POST', 'GET'])
def chem_comp():
    plot_Composition = plot_compos.composition_8elem()
    parse_elements = elements.elements_parser(random_session=RANDOM_SESS_KEY)
    print(request.method)
    print(request.form.get('redirect'))
    if request.method == 'POST':
        p_table,pong_table,selems,defaultab,no_of_elems = parse_elements.update_elements(request.form)
        if request.form.get("Update Plot"):
            defaultab = "Prediction-Tab"
            plot_script,plot_div,pelems,maxTc,comp_list = plot_Composition.update_plot(selems)
        else:
            defaultab = "Method-Tab"
            plot_script,plot_div,pelems,maxTc,comp_list = plot_Composition.old_plot()
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
                                custom_link=mylink)

    elif request.method == 'GET':
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
                                custom_link=mylink)
    
import glob
import os
import time
if __name__== '__main__':
    # cleaning old files
    files = glob.glob("elements_sess?_*.pkl")
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
    while RANDOM_SESS_KEY in fileSessKeys:
        RANDOM_SESS_KEY = f"{np.random.randint(0,999999):08d}"
    print(f"Session: {RANDOM_SESS_KEY}")
    parse_elements = elements.elements_parser(make_file=True, random_session=RANDOM_SESS_KEY)

    # app.run(port=8000, debug=True)
    app.run(port=33507)

