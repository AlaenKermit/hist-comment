import os
import time
def waittimer(x):
    time.sleep(x)
print("""
Linux käskude ajaloofaili automatiseeritud kommenteerija
ver 0.1 // Allan Kerme;Kristjan Kuus
""")
waittimer(3)
failinimi = str(input("""
NB: Faili formaat peab olema
käsk - ### kommentaar
Sisestage failinimi käskudega: """))
historyfail = str(input("Sisestage oma history failinimi, mille käsud soovite kommenteerida"))
historyfailavatud = open(historyfail, encoding="UTF-8")
failseletustega = open(failinimi, encoding="UTF-8")
for i in historyfailavatud:
    esimenesõna = i.split()[1]
    print(esimenesõna)
