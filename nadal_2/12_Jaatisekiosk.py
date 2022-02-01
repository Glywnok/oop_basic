from nadal_2.Jaatis import Restoraan
from nadal_2.Jaatis import Jaatisekiosk

nimi = str(input("Sisestage palun kioski nimi: "))
muuakse = str(input("Mida müüakse sel kioskis? "))
avatud = str(input("Kas kiosk on avatud? Kui jah siis sisestage jah/Jah "))

Jaatis_kiosk = Restoraan(nimi, muuakse)
Jaatise_kiosk = Jaatisekiosk(nimi, muuakse)


if avatud == "Jah" or "jah":
    Jaatis_kiosk.ava()
elif avatud == "Ei" or "ei":
    Jaatis_kiosk.kinni()
    exit()

Jaatise_kiosk.maara_jaatise_valik()
Jaatise_kiosk.jaatise_valik()

Jaatis_kiosk

