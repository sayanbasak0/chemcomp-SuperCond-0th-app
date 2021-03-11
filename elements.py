import pickle

class elements_parser:
    def __init__(self, make_file=False, random_session=-1):
        # load model and define global as class variables
        self.random_session = random_session
        if (make_file):
            with open(f'elements_sess1.pkl', 'rb') as f:
                sess_dict1 = pickle.load(f)
                self.list_2 = sess_dict1["list_2"]
                self.list_1 = sess_dict1["list_1"]
                self.dict_1 = sess_dict1["dict_1"]
                self.defaultab1 = sess_dict1["defaultab1"]
                self.no_of_elems1 = sess_dict1["no_of_elems1"]
                self.selected_elems1 = sess_dict1["selected_elems1"]
            with open(f'elements_sess2.pkl', 'rb') as f:
                sess_dict2 = pickle.load(f)
                self.list_1 = sess_dict2["list_1"]
                self.list_2 = sess_dict2["list_2"]
                self.dict_2 = sess_dict2["dict_2"]
                self.defaultab2 = sess_dict2["defaultab2"]
                self.no_of_elems2 = sess_dict2["no_of_elems2"]
                self.prop_of_elems2 = sess_dict2["prop_of_elems2"]
                self.selected_elems2 = sess_dict2["selected_elems2"]
            self.dict_1["B"] = 1
            self.dict_1["Mg"] = 1
            self.defaultab1 = "Periodic-Tab"
            self.no_of_elems1 = 4
            self.selected_elems1 = ["B,Mg"]

            self.dict_2["B"] = 0.67
            self.dict_2["Mg"] = 0.33
            self.defaultab2 = "Periodic-Tab"
            self.no_of_elems2 = 4
            self.prop_of_elems2 = 0.5
            self.selected_elems2 = {"B":0.67,"Mg":0.33}
            with open(f'elements_sess1_{self.random_session}.pkl', 'wb') as f:
                sess_dict1 = {}
                sess_dict1["list_1"] = self.list_1
                sess_dict1["dict_1"] = self.dict_1
                sess_dict1["defaultab1"] = self.defaultab1
                sess_dict1["no_of_elems1"] = self.no_of_elems1
                sess_dict1["selected_elems1"] = self.selected_elems1
                pickle.dump(sess_dict1, f)
            
            with open(f'elements_sess2_{self.random_session}.pkl', 'wb') as f:
                sess_dict2 = {}
                sess_dict2["list_2"] = self.list_2
                sess_dict2["dict_2"] = self.dict_2
                sess_dict2["defaultab2"] = self.defaultab2
                sess_dict2["no_of_elems2"] = self.no_of_elems2
                sess_dict2["prop_of_elems2"] = self.prop_of_elems2
                sess_dict2["selected_elems2"] = self.selected_elems2
                pickle.dump(sess_dict2, f)
        else:
            with open(f'elements_sess1_{self.random_session}.pkl', 'rb') as f:
                sess_dict1 = pickle.load(f)
                self.list_2 = sess_dict1["list_2"]
                self.list_1 = sess_dict1["list_1"]
                self.dict_1 = sess_dict1["dict_1"]
                self.defaultab1 = sess_dict1["defaultab1"]
                self.no_of_elems1 = sess_dict1["no_of_elems1"]
                self.selected_elems1 = sess_dict1["selected_elems1"]
            with open(f'elements_sess2_{self.random_session}.pkl', 'rb') as f:
                sess_dict2 = pickle.load(f)
                self.list_1 = sess_dict2["list_1"]
                self.list_2 = sess_dict2["list_2"]
                self.dict_2 = sess_dict2["dict_2"]
                self.defaultab2 = sess_dict2["defaultab2"]
                self.no_of_elems2 = sess_dict2["no_of_elems2"]
                self.prop_of_elems2 = sess_dict2["prop_of_elems2"]
                self.selected_elems2 = sess_dict2["selected_elems2"]

    def __del__(self):
        with open(f'elements_sess1_{self.random_session}.pkl', 'wb') as f:
            sess_dict1 = {}
            sess_dict1["list_2"] = self.list_2
            sess_dict1["list_1"] = self.list_1
            sess_dict1["dict_1"] = self.dict_1
            sess_dict1["defaultab1"] = self.defaultab1
            sess_dict1["no_of_elems1"] = self.no_of_elems1
            sess_dict1["selected_elems1"] = self.selected_elems1
            pickle.dump(sess_dict1, f)
        
        with open(f'elements_sess2_{self.random_session}.pkl', 'wb') as f:
            sess_dict2 = {}
            sess_dict2["list_1"] = self.list_1
            sess_dict2["list_2"] = self.list_2
            sess_dict2["dict_2"] = self.dict_2
            sess_dict2["defaultab2"] = self.defaultab2
            sess_dict2["no_of_elems2"] = self.no_of_elems2
            sess_dict2["prop_of_elems2"] = self.prop_of_elems2
            sess_dict2["selected_elems2"] = self.selected_elems2
            pickle.dump(sess_dict2, f)

    def update_elements(self,dict_new):
        
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
        
        return self.list_1,self.list_2,self.dict_1,self.defaultab1,self.no_of_elems1

    
    def update_composition(self,dict_new):
        
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
            self.defaultab2 = dict_new['Update Plot']
        
        return self.list_1,self.list_2,self.dict_2,self.defaultab2,self.no_of_elems2,self.prop_of_elems2