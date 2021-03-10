from flask import Flask,render_template,request,url_for,redirect
from bokeh.models.annotations import Title
from bokeh.plotting import figure,show
from bokeh.io import output_notebook
import numpy as np
from bokeh.embed import file_html,components
from bokeh.resources import CDN
import sys
import elements
import plot_temp

mylink = "/"
HEADING = "Searching for chemical compositions of Superconductors"
OFFLINE_DEBUG = False

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
    p_table = elements.list_1
    pong_table = elements.list_2
    print(request.method)
    print(request.form.get('redirect'))
    if request.method == 'POST':
        selems,defaultab,no_of_elems,prop_of_elems = elements.update_composition(request.form)
        if request.form.get("Update Plot"):
            plot_script,plot_div,pelems,maxTc,comp_list = plot_temp.update_plot(selems)
        else:
            plot_script,plot_div,pelems,maxTc,comp_list = plot_temp.old_plot()
        return render_template('crit_temp.html', 
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
                                prop_of_elems=prop_of_elems,
                                custom_link=mylink)

    elif request.method == 'GET':
        selems = elements.dict_2
        defaultab = "Periodic-Tab"
        no_of_elems = 4
        prop_of_elems = 0.5
        plot_script,plot_div,pelems,maxTc,comp_list = plot_temp.update_plot(selems)
        return render_template('crit_temp.html', 
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
                                prop_of_elems=prop_of_elems,
                                custom_link=mylink)

@app.route('/chem_comp',methods = ['POST', 'GET'])
def chem_comp():
    p_table = elements.list_1
    pong_table = elements.list_2
    print(request.method)
    print(request.form.get('redirect'))
    if request.method == 'POST':
        selems,defaultab,no_of_elems,prop_of_elems = elements.update_elements(request.form)
        if request.form.get("Update Plot"):
            plot_script,plot_div,pelems,maxTc,comp_list = plot_temp.update_plot(selems)
        else:
            plot_script,plot_div,pelems,maxTc,comp_list = plot_temp.old_plot()
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
                                prop_of_elems=prop_of_elems,
                                custom_link=mylink)

    elif request.method == 'GET':
        selems = elements.dict_2
        defaultab = "Periodic-Tab"
        no_of_elems = 4
        prop_of_elems = 0.5
        plot_script,plot_div,pelems,maxTc,comp_list = plot_temp.update_plot(selems)
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
                                prop_of_elems=prop_of_elems,
                                custom_link=mylink)
    
if __name__== '__main__':
    if len(sys.argv)>1:
        if sys.argv[1]=='local':
            OFFLINE_DEBUG = True
            plot_temp.load_model(OFFLINE_DEBUG)
            app.run(port=8000, debug=True)
        else:
            plot_temp.load_model(OFFLINE_DEBUG)
            app.run(port=8000, debug=True)
    else:
        plot_temp.load_model(OFFLINE_DEBUG)
        app.run(port=33507)

