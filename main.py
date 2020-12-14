import os
import time
print("""
.▄▄ ·  ▄▄▄·  ▄▄▄· ▄▄▄  ▄▄▄ .• ▌ ▄ ·.  ▄▄▄·  ▄▄▄·     ▄▄▌ ▐ ▄▌ ▄▄▄· ▄▄▄  .▄▄ · 
▐█ ▀. ▐█ ▀█ ▐█ ▀█ ▀▄ █·▀▄.▀··██ ▐███▪▐█ ▀█ ▐█ ▀█     ██· █▌▐█▐█ ▀█ ▀▄ █·▐█ ▀. 
▄▀▀▀█▄▄█▀▀█ ▄█▀▀█ ▐▀▀▄ ▐▀▀▪▄▐█ ▌▐▌▐█·▄█▀▀█ ▄█▀▀█     ██▪▐█▐▐▌▄█▀▀█ ▐▀▀▄ ▄▀▀▀█▄
▐█▄▪▐█▐█ ▪▐▌▐█ ▪▐▌▐█•█▌▐█▄▄▌██ ██▌▐█▌▐█ ▪▐▌▐█ ▪▐▌    ▐█▌██▐█▌▐█ ▪▐▌▐█•█▌▐█▄▪▐█
 ▀▀▀▀  ▀  ▀  ▀  ▀ .▀  ▀ ▀▀▀ ▀▀  █▪▀▀▀ ▀  ▀  ▀  ▀      ▀▀▀▀ ▀▪ ▀  ▀ .▀  ▀ ▀▀▀▀ 
ver 0.1                                              Allan Kerme;Kristjan Kuus
""")

time.sleep(3)

tegelasenimi = str(input("Sisestage oma tegelase nimi: "))
print("Kas olete kindel, et soovite oma tegelase nimeks panna", (tegelasenimi), "?")

kindel = str(input("jah või ei:? "))

if kindel == str("ei"):
    tegelasenimi = str(input("Sisestage oma tegelase nimi: "))
    print("Te olete muutnud oma tegelase nime,", tegelasenimi)
    
print("Palun valige oma tegelasklass:\nRÜÜTEL | VIBUKÜTT | MAAGIAMEISTER")
tegelasklass = str(input("Tegelasklass: "))
