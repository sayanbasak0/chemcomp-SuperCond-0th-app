import random
class elements_parser:
    def __init__(self):
        # load model and define global as class variables
        self.dict_1 = {}
        self.dict_2 = {}
        def gb1(elem):
            
            if elem not in ["An","Ln","arrow","space"]:
                if elem not in self.dict_1.keys():
                    self.dict_1[elem] = 0
                    self.dict_2[elem] = 0
            else:
                self.dict_1[elem] = -1
                self.dict_2[elem] = -1
                
            return elem

        self.list_1 = []

        # row 1
        self.list_1.append(gb1("H"))
        self.list_1.append(gb1("D"))
        self.list_1.append(gb1("T"))
        for i in range(14):
            self.list_1.append(gb1("space"))
        self.list_1.append(gb1("He"))

        # row 2
        self.list_1.append(gb1("Li"))
        self.list_1.append(gb1("Be"))
        for i in range(10):
            self.list_1.append(gb1("space"))
        self.list_1.append(gb1("B"))
        self.list_1.append(gb1("C"))
        self.list_1.append(gb1("N"))
        self.list_1.append(gb1("O"))
        self.list_1.append(gb1("F"))
        self.list_1.append(gb1("Ne"))

        # row 3
        self.list_1.append(gb1("Na"))
        self.list_1.append(gb1("Mg"))
        for i in range(10):
            self.list_1.append(gb1("space"))
        self.list_1.append(gb1("Al"))
        self.list_1.append(gb1("Si"))
        self.list_1.append(gb1("P"))
        self.list_1.append(gb1("S"))
        self.list_1.append(gb1("Cl"))
        self.list_1.append(gb1("Ar"))

        # row 4
        self.list_1.append(gb1("K"))
        self.list_1.append(gb1("Ca"))
        self.list_1.append(gb1("Sc"))
        self.list_1.append(gb1("Ti"))
        self.list_1.append(gb1("V"))
        self.list_1.append(gb1("Cr"))
        self.list_1.append(gb1("Mn"))
        self.list_1.append(gb1("Fe"))
        self.list_1.append(gb1("Co"))
        self.list_1.append(gb1("Ni"))
        self.list_1.append(gb1("Cu"))
        self.list_1.append(gb1("Zn"))
        self.list_1.append(gb1("Ga"))
        self.list_1.append(gb1("Ge"))
        self.list_1.append(gb1("As"))
        self.list_1.append(gb1("Se"))
        self.list_1.append(gb1("Br"))
        self.list_1.append(gb1("Kr"))

        # row 5
        self.list_1.append(gb1("Rb"))
        self.list_1.append(gb1("Sr"))
        self.list_1.append(gb1("Y"))
        self.list_1.append(gb1("Zr"))
        self.list_1.append(gb1("Nb"))
        self.list_1.append(gb1("Mo"))
        self.list_1.append(gb1("Tc"))
        self.list_1.append(gb1("Ru"))
        self.list_1.append(gb1("Rh"))
        self.list_1.append(gb1("Pd"))
        self.list_1.append(gb1("Ag"))
        self.list_1.append(gb1("Cd"))
        self.list_1.append(gb1("In"))
        self.list_1.append(gb1("Sn"))
        self.list_1.append(gb1("Sb"))
        self.list_1.append(gb1("Te"))
        self.list_1.append(gb1("I"))
        self.list_1.append(gb1("Xe"))

        # row 6
        self.list_1.append(gb1("Cs"))
        self.list_1.append(gb1("Ba"))
        self.list_1.append(gb1("Ln"))
        self.list_1.append(gb1("Hf"))
        self.list_1.append(gb1("Ta"))
        self.list_1.append(gb1("W"))
        self.list_1.append(gb1("Re"))
        self.list_1.append(gb1("Os"))
        self.list_1.append(gb1("Ir"))
        self.list_1.append(gb1("Pt"))
        self.list_1.append(gb1("Au"))
        self.list_1.append(gb1("Hg"))
        self.list_1.append(gb1("Tl"))
        self.list_1.append(gb1("Pb"))
        self.list_1.append(gb1("Bi"))
        self.list_1.append(gb1("Po"))
        self.list_1.append(gb1("At"))
        self.list_1.append(gb1("Rn"))

        # row 7
        self.list_1.append(gb1("Fr"))
        self.list_1.append(gb1("Ra"))
        self.list_1.append(gb1("An"))
        self.list_1.append(gb1("Rf"))
        self.list_1.append(gb1("Db"))
        self.list_1.append(gb1("Sg"))
        self.list_1.append(gb1("Bh"))
        self.list_1.append(gb1("Hs"))
        self.list_1.append(gb1("Mt"))
        self.list_1.append(gb1("Ds"))
        self.list_1.append(gb1("Rg"))
        self.list_1.append(gb1("Cn"))
        self.list_1.append(gb1("Nh"))
        self.list_1.append(gb1("Fl"))
        self.list_1.append(gb1("Mc"))
        self.list_1.append(gb1("Lv"))
        self.list_1.append(gb1("Ts"))
        self.list_1.append(gb1("Og"))

        # row 6-Ln
        self.list_1.append(gb1("space"))
        self.list_1.append(gb1("Ln"))
        self.list_1.append(gb1("arrow"))
        self.list_1.append(gb1("La"))
        self.list_1.append(gb1("Ce"))
        self.list_1.append(gb1("Pr"))
        self.list_1.append(gb1("Nd"))
        self.list_1.append(gb1("Pm"))
        self.list_1.append(gb1("Sm"))
        self.list_1.append(gb1("Eu"))
        self.list_1.append(gb1("Gd"))
        self.list_1.append(gb1("Tb"))
        self.list_1.append(gb1("Dy"))
        self.list_1.append(gb1("Ho"))
        self.list_1.append(gb1("Er"))
        self.list_1.append(gb1("Tm"))
        self.list_1.append(gb1("Yb"))
        self.list_1.append(gb1("Lu"))

        # row 7-An
        self.list_1.append(gb1("space"))
        self.list_1.append(gb1("An"))
        self.list_1.append(gb1("arrow"))
        self.list_1.append(gb1("Ac"))
        self.list_1.append(gb1("Th"))
        self.list_1.append(gb1("Pa"))
        self.list_1.append(gb1("U"))
        self.list_1.append(gb1("Np"))
        self.list_1.append(gb1("Pu"))
        self.list_1.append(gb1("Am"))
        self.list_1.append(gb1("Cm"))
        self.list_1.append(gb1("Bk"))
        self.list_1.append(gb1("Cf"))
        self.list_1.append(gb1("Es"))
        self.list_1.append(gb1("Fm"))
        self.list_1.append(gb1("Md"))
        self.list_1.append(gb1("No"))
        self.list_1.append(gb1("Lr"))

        self.list_2 = []

        # row 1
        self.list_2.append(gb1("H"))
        self.list_2.append(gb1("D"))
        self.list_2.append(gb1("T"))
        for i in range(28):
            self.list_2.append(gb1("space"))
        self.list_2.append(gb1("He"))

        # row 2
        self.list_2.append(gb1("Li"))
        self.list_2.append(gb1("Be"))
        for i in range(24):
            self.list_2.append(gb1("space"))
        self.list_2.append(gb1("B"))
        self.list_2.append(gb1("C"))
        self.list_2.append(gb1("N"))
        self.list_2.append(gb1("O"))
        self.list_2.append(gb1("F"))
        self.list_2.append(gb1("Ne"))

        # row 3
        self.list_2.append(gb1("Na"))
        self.list_2.append(gb1("Mg"))
        for i in range(24):
            self.list_2.append(gb1("space"))
        self.list_2.append(gb1("Al"))
        self.list_2.append(gb1("Si"))
        self.list_2.append(gb1("P"))
        self.list_2.append(gb1("S"))
        self.list_2.append(gb1("Cl"))
        self.list_2.append(gb1("Ar"))

        # row 4
        self.list_2.append(gb1("K"))
        self.list_2.append(gb1("Ca"))
        for i in range(14):
            self.list_2.append(gb1("space"))
        self.list_2.append(gb1("Sc"))
        self.list_2.append(gb1("Ti"))
        self.list_2.append(gb1("V"))
        self.list_2.append(gb1("Cr"))
        self.list_2.append(gb1("Mn"))
        self.list_2.append(gb1("Fe"))
        self.list_2.append(gb1("Co"))
        self.list_2.append(gb1("Ni"))
        self.list_2.append(gb1("Cu"))
        self.list_2.append(gb1("Zn"))
        self.list_2.append(gb1("Ga"))
        self.list_2.append(gb1("Ge"))
        self.list_2.append(gb1("As"))
        self.list_2.append(gb1("Se"))
        self.list_2.append(gb1("Br"))
        self.list_2.append(gb1("Kr"))

        # row 5
        self.list_2.append(gb1("Rb"))
        self.list_2.append(gb1("Sr"))
        for i in range(14):
            self.list_2.append(gb1("space"))
        self.list_2.append(gb1("Y"))
        self.list_2.append(gb1("Zr"))
        self.list_2.append(gb1("Nb"))
        self.list_2.append(gb1("Mo"))
        self.list_2.append(gb1("Tc"))
        self.list_2.append(gb1("Ru"))
        self.list_2.append(gb1("Rh"))
        self.list_2.append(gb1("Pd"))
        self.list_2.append(gb1("Ag"))
        self.list_2.append(gb1("Cd"))
        self.list_2.append(gb1("In"))
        self.list_2.append(gb1("Sn"))
        self.list_2.append(gb1("Sb"))
        self.list_2.append(gb1("Te"))
        self.list_2.append(gb1("I"))
        self.list_2.append(gb1("Xe"))

        # row 6
        self.list_2.append(gb1("Cs"))
        self.list_2.append(gb1("Ba"))

        # row 6-Ln
        self.list_2.append(gb1("La"))
        self.list_2.append(gb1("Ce"))
        self.list_2.append(gb1("Pr"))
        self.list_2.append(gb1("Nd"))
        self.list_2.append(gb1("Pm"))
        self.list_2.append(gb1("Sm"))
        self.list_2.append(gb1("Eu"))
        self.list_2.append(gb1("Gd"))
        self.list_2.append(gb1("Tb"))
        self.list_2.append(gb1("Dy"))
        self.list_2.append(gb1("Ho"))
        self.list_2.append(gb1("Er"))
        self.list_2.append(gb1("Tm"))
        self.list_2.append(gb1("Yb"))
        self.list_2.append(gb1("Lu"))

        self.list_2.append(gb1("Hf"))
        self.list_2.append(gb1("Ta"))
        self.list_2.append(gb1("W"))
        self.list_2.append(gb1("Re"))
        self.list_2.append(gb1("Os"))
        self.list_2.append(gb1("Ir"))
        self.list_2.append(gb1("Pt"))
        self.list_2.append(gb1("Au"))
        self.list_2.append(gb1("Hg"))
        self.list_2.append(gb1("Tl"))
        self.list_2.append(gb1("Pb"))
        self.list_2.append(gb1("Bi"))
        self.list_2.append(gb1("Po"))
        self.list_2.append(gb1("At"))
        self.list_2.append(gb1("Rn"))

        # row 7
        self.list_2.append(gb1("Fr"))
        self.list_2.append(gb1("Ra"))

        # row 7-An
        self.list_2.append(gb1("Ac"))
        self.list_2.append(gb1("Th"))
        self.list_2.append(gb1("Pa"))
        self.list_2.append(gb1("U"))
        self.list_2.append(gb1("Np"))
        self.list_2.append(gb1("Pu"))
        self.list_2.append(gb1("Am"))
        self.list_2.append(gb1("Cm"))
        self.list_2.append(gb1("Bk"))
        self.list_2.append(gb1("Cf"))
        self.list_2.append(gb1("Es"))
        self.list_2.append(gb1("Fm"))
        self.list_2.append(gb1("Md"))
        self.list_2.append(gb1("No"))
        self.list_2.append(gb1("Lr"))

        self.list_2.append(gb1("Rf"))
        self.list_2.append(gb1("Db"))
        self.list_2.append(gb1("Sg"))
        self.list_2.append(gb1("Bh"))
        self.list_2.append(gb1("Hs"))
        self.list_2.append(gb1("Mt"))
        self.list_2.append(gb1("Ds"))
        self.list_2.append(gb1("Rg"))
        self.list_2.append(gb1("Cn"))
        self.list_2.append(gb1("Nh"))
        self.list_2.append(gb1("Fl"))
        self.list_2.append(gb1("Mc"))
        self.list_2.append(gb1("Lv"))
        self.list_2.append(gb1("Ts"))
        self.list_2.append(gb1("Og"))

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
            
        return self.dict_1,self.defaultab1,self.no_of_elems1

    
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
            
        return self.dict_2,self.defaultab2,self.no_of_elems2,self.prop_of_elems2