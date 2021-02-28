import random

dict_1 = {}
dict_2 = {}
pos_ = {}
count_1 = 0
def gb1(elem):
    global count_1
    if elem not in ["An","Ln","arrow","space"]:
        if elem not in dict_1.keys():
            dict_1[elem] = 1
            dict_2[elem] = 1
            pos_[elem] = [count_1,0]
        else:
            pos_[elem][0] = count_1
    else:
        dict_1[elem] = -1
        dict_2[elem] = -1
        

    count_1 += 1
    return elem

count_2 = 0
def gb2(elem):
    global count_2
    if elem not in ["An","Ln","arrow","space"]:
        if elem not in dict_1.keys():
            dict_1[elem] = 1
            dict_2[elem] = 1
            pos_[elem] = [count_2,0]
        else:
            pos_[elem][0] = count_2
    else:
            dict_1[elem] = -1
            dict_2[elem] = -1
    count_2 += 1
    return elem

list_1 = []

# row 1
list_1.append(gb1("H"))
list_1.append(gb1("D"))
list_1.append(gb1("T"))
for i in range(14):
    list_1.append(gb1("space"))
list_1.append(gb1("He"))

# row 2
list_1.append(gb1("Li"))
list_1.append(gb1("Be"))
for i in range(10):
    list_1.append(gb1("space"))
list_1.append(gb1("B"))
list_1.append(gb1("C"))
list_1.append(gb1("N"))
list_1.append(gb1("O"))
list_1.append(gb1("F"))
list_1.append(gb1("Ne"))

# row 3
list_1.append(gb1("Na"))
list_1.append(gb1("Mg"))
for i in range(10):
    list_1.append(gb1("space"))
list_1.append(gb1("Al"))
list_1.append(gb1("Si"))
list_1.append(gb1("P"))
list_1.append(gb1("S"))
list_1.append(gb1("Cl"))
list_1.append(gb1("Ar"))

# row 4
list_1.append(gb1("K"))
list_1.append(gb1("Ca"))
list_1.append(gb1("Sc"))
list_1.append(gb1("Ti"))
list_1.append(gb1("V"))
list_1.append(gb1("Cr"))
list_1.append(gb1("Mn"))
list_1.append(gb1("Fe"))
list_1.append(gb1("Co"))
list_1.append(gb1("Ni"))
list_1.append(gb1("Cu"))
list_1.append(gb1("Zn"))
list_1.append(gb1("Ga"))
list_1.append(gb1("Ge"))
list_1.append(gb1("As"))
list_1.append(gb1("Se"))
list_1.append(gb1("Br"))
list_1.append(gb1("Kr"))

# row 5
list_1.append(gb1("Rb"))
list_1.append(gb1("Sr"))
list_1.append(gb1("Y"))
list_1.append(gb1("Zr"))
list_1.append(gb1("Nb"))
list_1.append(gb1("Mo"))
list_1.append(gb1("Tc"))
list_1.append(gb1("Ru"))
list_1.append(gb1("Rh"))
list_1.append(gb1("Pd"))
list_1.append(gb1("Ag"))
list_1.append(gb1("Cd"))
list_1.append(gb1("In"))
list_1.append(gb1("Sn"))
list_1.append(gb1("Sb"))
list_1.append(gb1("Te"))
list_1.append(gb1("I"))
list_1.append(gb1("Xe"))

# row 6
list_1.append(gb1("Cs"))
list_1.append(gb1("Ba"))
list_1.append(gb1("Ln"))
list_1.append(gb1("Hf"))
list_1.append(gb1("Ta"))
list_1.append(gb1("W"))
list_1.append(gb1("Re"))
list_1.append(gb1("Os"))
list_1.append(gb1("Ir"))
list_1.append(gb1("Pt"))
list_1.append(gb1("Au"))
list_1.append(gb1("Hg"))
list_1.append(gb1("Tl"))
list_1.append(gb1("Pb"))
list_1.append(gb1("Bi"))
list_1.append(gb1("Po"))
list_1.append(gb1("At"))
list_1.append(gb1("Rn"))

# row 7
list_1.append(gb1("Fr"))
list_1.append(gb1("Ra"))
list_1.append(gb1("An"))
list_1.append(gb1("Rf"))
list_1.append(gb1("Db"))
list_1.append(gb1("Sg"))
list_1.append(gb1("Bh"))
list_1.append(gb1("Hs"))
list_1.append(gb1("Mt"))
list_1.append(gb1("Ds"))
list_1.append(gb1("Rg"))
list_1.append(gb1("Cn"))
list_1.append(gb1("Nh"))
list_1.append(gb1("Fl"))
list_1.append(gb1("Mc"))
list_1.append(gb1("Lv"))
list_1.append(gb1("Ts"))
list_1.append(gb1("Og"))

# row 6-Ln
list_1.append(gb1("space"))
list_1.append(gb1("Ln"))
list_1.append(gb1("arrow"))
list_1.append(gb1("La"))
list_1.append(gb1("Ce"))
list_1.append(gb1("Pr"))
list_1.append(gb1("Nd"))
list_1.append(gb1("Pm"))
list_1.append(gb1("Sm"))
list_1.append(gb1("Eu"))
list_1.append(gb1("Gd"))
list_1.append(gb1("Tb"))
list_1.append(gb1("Dy"))
list_1.append(gb1("Ho"))
list_1.append(gb1("Er"))
list_1.append(gb1("Tm"))
list_1.append(gb1("Yb"))
list_1.append(gb1("Lu"))

# row 7-An
list_1.append(gb1("space"))
list_1.append(gb1("An"))
list_1.append(gb1("arrow"))
list_1.append(gb1("Ac"))
list_1.append(gb1("Th"))
list_1.append(gb1("Pa"))
list_1.append(gb1("U"))
list_1.append(gb1("Np"))
list_1.append(gb1("Pu"))
list_1.append(gb1("Am"))
list_1.append(gb1("Cm"))
list_1.append(gb1("Bk"))
list_1.append(gb1("Cf"))
list_1.append(gb1("Es"))
list_1.append(gb1("Fm"))
list_1.append(gb1("Md"))
list_1.append(gb1("No"))
list_1.append(gb1("Lr"))

list_2 = []

# row 1
list_2.append(gb1("H"))
list_2.append(gb1("D"))
list_2.append(gb1("T"))
for i in range(28):
    list_2.append(gb1("space"))
list_2.append(gb1("He"))

# row 2
list_2.append(gb1("Li"))
list_2.append(gb1("Be"))
for i in range(24):
    list_2.append(gb1("space"))
list_2.append(gb1("B"))
list_2.append(gb1("C"))
list_2.append(gb1("N"))
list_2.append(gb1("O"))
list_2.append(gb1("F"))
list_2.append(gb1("Ne"))

# row 3
list_2.append(gb1("Na"))
list_2.append(gb1("Mg"))
for i in range(24):
    list_2.append(gb1("space"))
list_2.append(gb1("Al"))
list_2.append(gb1("Si"))
list_2.append(gb1("P"))
list_2.append(gb1("S"))
list_2.append(gb1("Cl"))
list_2.append(gb1("Ar"))

# row 4
list_2.append(gb1("K"))
list_2.append(gb1("Ca"))
for i in range(14):
    list_2.append(gb1("space"))
list_2.append(gb1("Sc"))
list_2.append(gb1("Ti"))
list_2.append(gb1("V"))
list_2.append(gb1("Cr"))
list_2.append(gb1("Mn"))
list_2.append(gb1("Fe"))
list_2.append(gb1("Co"))
list_2.append(gb1("Ni"))
list_2.append(gb1("Cu"))
list_2.append(gb1("Zn"))
list_2.append(gb1("Ga"))
list_2.append(gb1("Ge"))
list_2.append(gb1("As"))
list_2.append(gb1("Se"))
list_2.append(gb1("Br"))
list_2.append(gb1("Kr"))

# row 5
list_2.append(gb1("Rb"))
list_2.append(gb1("Sr"))
for i in range(14):
    list_2.append(gb1("space"))
list_2.append(gb1("Y"))
list_2.append(gb1("Zr"))
list_2.append(gb1("Nb"))
list_2.append(gb1("Mo"))
list_2.append(gb1("Tc"))
list_2.append(gb1("Ru"))
list_2.append(gb1("Rh"))
list_2.append(gb1("Pd"))
list_2.append(gb1("Ag"))
list_2.append(gb1("Cd"))
list_2.append(gb1("In"))
list_2.append(gb1("Sn"))
list_2.append(gb1("Sb"))
list_2.append(gb1("Te"))
list_2.append(gb1("I"))
list_2.append(gb1("Xe"))

# row 6
list_2.append(gb1("Cs"))
list_2.append(gb1("Ba"))

# row 6-Ln
list_2.append(gb1("La"))
list_2.append(gb1("Ce"))
list_2.append(gb1("Pr"))
list_2.append(gb1("Nd"))
list_2.append(gb1("Pm"))
list_2.append(gb1("Sm"))
list_2.append(gb1("Eu"))
list_2.append(gb1("Gd"))
list_2.append(gb1("Tb"))
list_2.append(gb1("Dy"))
list_2.append(gb1("Ho"))
list_2.append(gb1("Er"))
list_2.append(gb1("Tm"))
list_2.append(gb1("Yb"))
list_2.append(gb1("Lu"))

list_2.append(gb1("Hf"))
list_2.append(gb1("Ta"))
list_2.append(gb1("W"))
list_2.append(gb1("Re"))
list_2.append(gb1("Os"))
list_2.append(gb1("Ir"))
list_2.append(gb1("Pt"))
list_2.append(gb1("Au"))
list_2.append(gb1("Hg"))
list_2.append(gb1("Tl"))
list_2.append(gb1("Pb"))
list_2.append(gb1("Bi"))
list_2.append(gb1("Po"))
list_2.append(gb1("At"))
list_2.append(gb1("Rn"))

# row 7
list_2.append(gb1("Fr"))
list_2.append(gb1("Ra"))

# row 7-An
list_2.append(gb1("Ac"))
list_2.append(gb1("Th"))
list_2.append(gb1("Pa"))
list_2.append(gb1("U"))
list_2.append(gb1("Np"))
list_2.append(gb1("Pu"))
list_2.append(gb1("Am"))
list_2.append(gb1("Cm"))
list_2.append(gb1("Bk"))
list_2.append(gb1("Cf"))
list_2.append(gb1("Es"))
list_2.append(gb1("Fm"))
list_2.append(gb1("Md"))
list_2.append(gb1("No"))
list_2.append(gb1("Lr"))

list_2.append(gb1("Rf"))
list_2.append(gb1("Db"))
list_2.append(gb1("Sg"))
list_2.append(gb1("Bh"))
list_2.append(gb1("Hs"))
list_2.append(gb1("Mt"))
list_2.append(gb1("Ds"))
list_2.append(gb1("Rg"))
list_2.append(gb1("Cn"))
list_2.append(gb1("Nh"))
list_2.append(gb1("Fl"))
list_2.append(gb1("Mc"))
list_2.append(gb1("Lv"))
list_2.append(gb1("Ts"))
list_2.append(gb1("Og"))


defaultab1 = "Periodic-Tab"
no_of_elems1 = 4
prop_of_elems1 = 0.5
def update_elements(dict_new):
    global dict_1,defaultab1,no_of_elems1,prop_of_elems1
    selected_elems = dict_new.get('Selected Elements').split(',')
    if dict_new.get('number of elems'):
        no_of_elems = int(dict_new.get('number of elems'))
    if dict_new.get('prop of elems'):
        prop_of_elems = float(dict_new.get('prop of elems'))
    if dict_new.get('Update Plot'):
        defaultab = dict_new['Update Plot']
        for dkey in dict_1.keys():
            if dkey in selected_elems:
                dict_1[dkey] = 1
            elif dict_1[dkey]!=-1:
                dict_1[dkey] = 0
    return dict_1,defaultab1,no_of_elems1,prop_of_elems1

defaultab2 = "Periodic-Tab"
no_of_elems2 = 4
prop_of_elems2 = 0.5
def update_composition(dict_new):
    global dict_2,defaultab2,no_of_elems2,prop_of_elems2
    selected_elems = {elem:float(prop) for elem_prop in dict_new.get('Selected Elements').split(',') for elem, prop in elem_prop.split('_')}
    if dict_new.get('number of elems'):
        no_of_elems = int(dict_new.get('number of elems'))
    if dict_new.get('prop of elems'):
        prop_of_elems = float(dict_new.get('prop of elems'))
    if dict_new.get('Update Plot'):
        defaultab = dict_new['Update Plot']
        for dkey in dict_2.keys():
            if dkey in selected_elems:
                dict_2[dkey] = selected_elems[dkey]
            elif dict_2[dkey]!=-1:
                dict_2[dkey] = 0
    return dict_2,defaultab,no_of_elems,prop_of_elems