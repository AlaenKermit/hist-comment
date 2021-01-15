# Autorid: Allan Kerme & Kristjan Kuus, Tartu Kutsehariduskeskus, ITS20
# Õpetaja tahab, et kommenteeritakse failid millesse väljendatakse
# Linuxi 'history' käsk. Meie mõtlesime, et me saaks teha automiseeritud
# skripti, mis teeks seda automaatselt meie eest.
#
# Programm küsib kasutajalt
# * millisest failist lugeda erinevatele käskudele kommentaarid
# * millise faili sisu hakata kommenteerima (eg history fail)
# * küsib kasutajalt mis hakkab uueks failinimeks kuhu kirjutatakse
# kommenteeritud sisu.
# Versioon 0.5A
import time # A   e   g
def waittimer(x): # kerge funtsioon
    time.sleep(x) #

def mainfunction():
    with open(uusfailinimi, "w") as outfile:
        for hist1 in historyreadlines:
            hist123 = hist1.strip().rstrip()
            hist4 = hist123.split(' ', 3)[2]
            for käsk1 in käsufailreadlines:
                käsk2 = käsk1.split(' ', 1)[0]
                if  hist4 == käsk2:
                   outfile.write(hist123 + " " + käsk1.split(' ', 1)[1])
                else:
                    waittimer(0.01)
                    print(hist123 + "   ei klapi   " + käsk1)
                
print("""
Linux käskude ajaloofaili automatiseeritud kommenteerija
ver 0.5A // Allan Kerme;Kristjan Kuus
""")

waittimer(2)

käsufail= str(input("""
NB: Käskude faili formaat peab olema
`käsk - ### kommentaar`
Sisestage failinimi käskudega: """))
historyfail = str(input("Sisestage oma history failinimi, mille käsud soovite kommenteerida: "))

historyfailavatud = open(historyfail, encoding="UTF-8")

käsufailavatud = open(käsufail, encoding="UTF-8")

historyreadlines = historyfailavatud.readlines()
käsufailreadlines = käsufailavatud.readlines()
uusfailinimi = str(input("Mis soovite uue faili nimeks, kuhu kirjutatakse muudatused?: "))
if uusfailinimi[-4:] == ".txt":
    print("Leidsin .txt lõpu failist, jätkan")
    mainfunction()
else:
    uusfailinimi = uusfailinimi + ".txt"
    mainfunction()
