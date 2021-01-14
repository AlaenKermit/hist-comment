import os
import time
def waittimer(x):
    time.sleep(x)
    
print("""
Linux käskude ajaloofaili automatiseeritud kommenteerija
ver 0.1 // Allan Kerme;Kristjan Kuus
""")

#waittimer(3)

käsufail= str(input("""
NB: Faili formaat peab olema
käsk - ### kommentaar
Sisestage failinimi käskudega: """))

historyfail = str(input("Sisestage oma history failinimi, mille käsud soovite kommenteerida: "))

historyfailavatud = open(historyfail, encoding="UTF-8")

käsufailavatud = open(käsufail, encoding="UTF-8")

historyreadlines = historyfailavatud.readlines()
käsufailreadlines = käsufailavatud.readlines()

with open("komenteeritudajalugu.txt", "w") as outfile:
    for hist1 in historyreadlines:
        hist123 = hist1.strip().rstrip().strip("\n")
        for käsk1 in käsufailreadlines:
            if  hist123[1] ==  len(käsk1[0]):
               outfile.write(hist123 + käsk1)
            else:
                print(hist123 + "   ei klapi   " + käsk1)
                

#for i in historyfailavatud:
#esimenesõna = i.split()[1]
#print(esimenesõna)
