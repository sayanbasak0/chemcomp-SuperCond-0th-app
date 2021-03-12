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
            with open(os.path.join(module_path,"data","temp",f"elements_sess1_{sekey}.pkl"), 'rb') as f:
                sess_dict1 = pickle.load(f)
        else:
            with open(os.path.join(module_path,"data",f"elements_sess1.pkl"), 'rb') as f:
                sess_dict1 = pickle.load(f)
        
        self.list_2 = sess_dict1["list_2"]
        self.list_1 = sess_dict1["list_1"]
        self.dict_1 = sess_dict1["dict_1"]
        self.defaultab1 = sess_dict1["defaultab1"]
        self.no_of_elems1 = sess_dict1["no_of_elems1"]
        self.selected_elems1 = sess_dict1["selected_elems1"]
        if not sekey:
            self.dict_1["B"] = 1
            self.dict_1["Mg"] = 1
            self.defaultab1 = "Periodic-Tab"
            self.no_of_elems1 = 4
            self.selected_elems1 = ["B,Mg"]

    def save(self, sekey=""):
        sess_dict1 = {}
        sess_dict1["list_2"] = self.list_2
        sess_dict1["list_1"] = self.list_1
        sess_dict1["dict_1"] = self.dict_1
        sess_dict1["defaultab1"] = self.defaultab1
        sess_dict1["no_of_elems1"] = self.no_of_elems1
        sess_dict1["selected_elems1"] = self.selected_elems1
        with open(os.path.join(module_path,"data","temp",f"elements_sess1_{sekey}.pkl"), 'wb') as f:
            pickle.dump(sess_dict1, f)
    
    def update_elements(self,dict_new):
        self.load(f'{self.random_session}')
        if dict_new.get('Selected Elements'):
            self.selected_elems1 = dict_new.get('Selected Elements').split(',')
            for dkey in self.dict_1.keys():
                if dkey in self.selected_elems1:
                    self.dict_1[dkey] = 1
                elif self.dict_1[dkey]!=-1:
                    self.dict_1[dkey] = 0
        if dict_new.get('number of elems'):
            self.no_of_elems1 = int(dict_new.get('number of elems'))
        if dict_new.get('Update Plot'):
            self.defaultab1 = dict_new['Update Plot']
        self.save(f'{self.random_session}')
        return self.list_1,self.list_2,self.dict_1,self.defaultab1,self.no_of_elems1
