import os
import time
def waittimer(x):
    time.sleep(x)
    
print("""
Linux käskude ajaloofaili automatiseeritud kommenteerija
ver 0.4 // Allan Kerme;Kristjan Kuus
""")

waittimer(3)

käsufail= str(input("""
NB: Käskude faili formaat peab olema
`käsk - ### kommentaar`
Sisestage failinimi käskudega: """))
historyfail = str(input("Sisestage oma history failinimi, mille käsud soovite kommenteerida: "))

historyfailavatud = open(historyfail, encoding="UTF-8")

käsufailavatud = open(käsufail, encoding="UTF-8")

historyreadlines = historyfailavatud.readlines()
käsufailreadlines = käsufailavatud.readlines()

with open("komenteeritudajalugu.txt", "w") as outfile:
    for hist1 in historyreadlines:
        hist123 = hist1.strip().rstrip().strip("\n")
        hist4 = hist123.split(' ', 3)[2]
        for käsk1 in käsufailreadlines:
            käsk2 = käsk1.split(' ', 1)[0]
            if  hist4 == käsk2:
               outfile.write(hist123 + " " + käsk1.split(' ', 1)[1])
            else:
                waittimer(0.01)
                print(hist123 + "   ei klapi   " + käsk1)
