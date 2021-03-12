import pickle
import os
module_path = os.path.split(__file__)[0]

class elements_parser:
    def __init__(self, make_file=False, random_session=-1):
        # load model and define global as class variables
        self.random_session = random_session
        
        if not(make_file):
            try:
                self.load(f'{self.random_session}')
            except Exception:
                self.load()
        else:
            self.load()
        self.save(f'{self.random_session}')

    def load(self, sekey=""):
        if sekey:
            with open(os.path.join(module_path,"data","temp",f"elements_sess2_{sekey}.pkl"), 'rb') as f:
                sess_dict2 = pickle.load(f)
        else:
            with open(os.path.join(module_path,"data",f"elements_sess2.pkl"), 'rb') as f:
                sess_dict2 = pickle.load(f)
        
        self.list_1 = sess_dict2["list_1"]
        self.list_2 = sess_dict2["list_2"]
        self.dict_2 = sess_dict2["dict_2"]
        self.defaultab2 = sess_dict2["defaultab2"]
        self.no_of_elems2 = sess_dict2["no_of_elems2"]
        self.prop_of_elems2 = sess_dict2["prop_of_elems2"]
        self.selected_elems2 = sess_dict2["selected_elems2"]
        if not sekey:
            self.dict_2["B"] = 0.67
            self.dict_2["Mg"] = 0.33
            self.defaultab2 = "Periodic-Tab"
            self.no_of_elems2 = 4
            self.prop_of_elems2 = 0.5
            self.selected_elems2 = {"B":0.67,"Mg":0.33}
    def save(self, sekey=""):
        sess_dict2 = {}
        sess_dict2["list_1"] = self.list_1
        sess_dict2["list_2"] = self.list_2
        sess_dict2["dict_2"] = self.dict_2
        sess_dict2["defaultab2"] = self.defaultab2
        sess_dict2["no_of_elems2"] = self.no_of_elems2
        sess_dict2["prop_of_elems2"] = self.prop_of_elems2
        sess_dict2["selected_elems2"] = self.selected_elems2
        os.makedirs(os.path.join(module_path,"data","temp"), exist_ok=True)
        with open(os.path.join(module_path,"data","temp",f"elements_sess2_{sekey}.pkl"), 'wb') as f:
            pickle.dump(sess_dict2, f)
        
    def update_composition(self,dict_new):
        self.load(f'{self.random_session}')
        if dict_new.get('Chemical Formula'):
            self.selected_elems2 = {elem_prop.split('_')[0]:float(elem_prop.split('_')[1]) for elem_prop in dict_new.get('Chemical Formula').strip(",").split(',') }
            for dkey in self.dict_2.keys():
                if dkey in self.selected_elems2:
                    self.dict_2[dkey] = self.selected_elems2[dkey]
                elif self.dict_2[dkey]!=-1:
                    self.dict_2[dkey] = 0
        if dict_new.get('number of elems'):
            self.no_of_elems2 = int(dict_new.get('number of elems'))
        if dict_new.get('prop of elems'):
            self.prop_of_elems2 = float(dict_new.get('prop of elems'))
        if dict_new.get('Update Plot'):
            # self.defaultab2 = dict_new['Update Plot']
            self.defaultab2 = "Prediction-Tab"
        elif dict_new.get('Critical Temperature redirect'):
            self.defaultab2 = "Prediction-Tab" 
        self.save(f'{self.random_session}')
        return self.list_1,self.list_2,self.dict_2,self.defaultab2,self.no_of_elems2,self.prop_of_elems2