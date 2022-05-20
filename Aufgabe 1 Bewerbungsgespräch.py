
from turtle import color


string1 = 'UIBAZDBSIAHFBC'
string2 = 'PQACIZDBIBDLAG'
string3 = 'QIDBCZDBKSHDVF'

def vergleich():
    greatest = ''
    for i in range(len(string1) -1):
        x = string1[i] + string1[i+1]
        if (x in string2 and x in string3):
            for a in range(len(string1) -1):
                t = a+2
                test = string1[i:t]
                if(test in string2 and test in string3):
                    if (len(test) > len(greatest)):
                        greatest = test
                else: 
                    break
    print(greatest)

#vergleich()



def challenge2():
    color = 'rbggbr'
    zaehlerRot = 0
    zaehlerBlau = 0
    zaehlerGruen = 0
    zaehler = 0

    m1 = 'rbg'
    m2 = 'rgb'
    m3 = 'bgr'
    m4 = 'brg'
    m5 = 'grb'
    m6 = 'gbr'

    for i in range(len(color)):
        x = color[i]
        if x in ['r']:
            zaehlerRot +=1
            continue
        elif x in ['b']:
            zaehlerBlau +=1
            continue
        elif x in ['g']:
            zaehlerGruen +=1
            continue
    if(zaehlerRot == zaehlerBlau and zaehlerRot == zaehlerGruen):
        zaehler +=1
        for a in range(len(color)-2):
            y = color[a] + color[a+1] + color[a+2]
            if(y == m1 or y == m2 or y == m3 or y == m4 or y == m5 or y == m6):
                zaehler +=1
            else:
                continue
    print(zaehler)
            
            
challenge2()