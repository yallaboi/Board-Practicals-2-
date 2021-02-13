#Question Bank Q5.(Files)

def AEcount():
    f=open("IMP.TXT","r")
    A,E=0,0
    r=f.read()
    for x in r:
        if x=='A' or x=='a':
            A=A+1
        elif x=="E" or x=="e":
            E=E+1
    f.close()
    print("'A' or 'a' occurs",A,"times")
    print("'E' or 'e'occurs",E,"times")

AEcount()
