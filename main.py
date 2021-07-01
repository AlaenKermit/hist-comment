##################################################################################
#                                                                                #
# Õpetaja tahab, et kommenteeritakse failid millesse suunatakse                  #
# Linuxi 'history' käsu väljund. Meie mõtlesime, et me saaks teha                #
# skripti, mis teeks seda automaatselt meie eest.                                #
#                                                                                #
##################################################################################
#                                                                   #
# Programm küsib kasutajalt                                         #
# * millisest failist lugeda erinevatele käskudele kommentaarid     #
# * millise faili sisu hakata kommenteerima (eg history fail)       #
# * küsib kasutajalt mis hakkab uueks failinimeks kuhu kirjutatakse #
# kommenteeritud sisu.                                              #
# Versioon 0.7.0                                                    #
#                                                                   #
#####################################################################
#                                       #
# Väga pointless funktsioon tegelikult. #
#                                       #
#########################################
import time # Aeg
def waittimer(x): # Ei midagi huvitavat pole öelda selle
    time.sleep(x) # funktsiooniga.
#####################################################################
#                                                                   #
# Peamine funktsioon, mille ülesandeks on siis võrrelda kahte faili #
# ja kui käskudefailist leiab vaste, siis ta lisab selle uude faili #
# koos kommentaariga.                                               #
#                                                                   #
#####################################################################
def mainfunction(x):
    with open(x, "w") as outfile:
        for hist1 in historyreadlines:
            hist123 = hist1.strip().rstrip()
            hist4 = hist123.split(' ', 3)[2]
            for käsk1 in käsufailreadlines:
                käsk2 = käsk1.split(' ', 1)[0]
                if  hist4 == käsk2:
                    outfile.write(hist123 + " " + käsk1.split(' ', 1)[1])
                else:
                    waittimer(0.01)
                    print(hist123 + "   ei klapi   " + käsk1 + "-ga")
#################################################################
#                                                               #
# Teine funktsioon, mis siis küsib kasutajalt, mis ta uue faili #
# nimeks soovib, ja kui sisendis on puudu .txt siis lisab       #
# selle. Kui ei ole puudu, siis jätkab nagu tavaliselt.         #
#                                                               #
#################################################################
def namefunction():
    uusfailinimi = str(input("Mis soovite uue faili nimeks, kuhu kirjutatakse muudatused?: "))
    if uusfailinimi[-4:] == ".txt":
        print("Failinimi lõpeb .txt-ga, jätkan")
        mainfunction(uusfailinimi)
    else:
        uusfailinimi += ".txt"
        mainfunction(uusfailinimi)

##############################################
# MMb     dMM      dM.       MM   MM\      M #
# MMM.   ,PMM     ,MMb       MM   MMM\     M #
# M`Mb   d'MM     d'YM.      MM   M\MM\    M #
# M YM. ,P MM    ,P `Mb      MM   M \MM\   M #
# M `Mb d' MM    d'  YM.     MM   M  \MM\  M #
# M  YM.P  MM   ,P   `Mb     MM   M   \MM\ M #
# M  `Mb'  MM   d'    YM.    MM   M    \MM\M #
# M   YP   MM  ,MMMMMMMMb    MM   M     \MMM #
# M   `'   MM  d'      YM.   MM   M      \MM #
# M        MM dM       dMM   MM   M       \M #
##############################################
#                                    #
# Lihtsalt visuaalne asjake alguses. #
#                                    #
######################################
print("""
Linux käskude ajaloofaili automatiseeritud kommenteerija
Versioon 0.7.0 // Allan Kerme | Kristjan Kuus
""")

waittimer(1)

käsufail= str(input("""
NB: Käskude faili formaat peab olema
`käsk - ### kommentaar`
Sisestage failinimi käskudega: """))
#################################################################
#                                                               #
# History failinime päring, mida kasutaja soovib kommenteerida. #
#                                                               #
#################################################################
historyfail = str(input("Sisestage oma history failinimi, mille käsud soovite kommenteerida: "))
###############################################################################
#                                                                             #
# Avame history & käsufailid, võtame nendes olevad read ja paneme need kinni. #
#                                                                             #
###############################################################################
historyfailavatud = open(historyfail, encoding="UTF-8")
käsufailavatud = open(käsufail, encoding="UTF-8")
historyreadlines = historyfailavatud.readlines()
käsufailreadlines = käsufailavatud.readlines()
historyfailavatud.close()
käsufailavatud.close()
################################################
#                                              #
# Käivitame namefunction nimelise funktsiooni. #
#                                              #
################################################
namefunction()
