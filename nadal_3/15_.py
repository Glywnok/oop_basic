from nadal_3.Kasutaja import Kasutaja
import time
password = "qwerty"
nimi = str(input(("Tere!\nPalun sisestage oma kasutaja nimet: ")))

print("Teie parool on juba määratud, kui te tahate teda muuta palun sisestage järgmised andmed: ")

katsed_suurendamine = int(input("On võimalik, et te ei mäleta oma parooli, ja te tahate suurendada parooli sisselogimis katseid: siis kui palju te tahate et see arv suurenes? "))
katsed = int(input("Maksimaalne arv katse: "))
print("Te olete sisetanud andmed mis on vaja, nüüd oodake.")
time.sleep(4)
Kasutaja1 = Kasutaja(nimi, katsed_suurendamine, katsed, password)

setup = Kasutaja1.password_test()
time.sleep(2)
print("Nüüd te võite vahetata oma parooli, kui tahate. ")
time.sleep(2)
ask1 = input(str("Kas te tahate vahetada oma parooli? Jah/jah või Ei/ei "))

if ask1 == "Jah" or "jah":
    new_password = Kasutaja1.NEW_PASS(setup)
    Kasutaja1.set_password(new_password)


print("Nüüd vaatame teie parooli ja kasutajanimele!")

time.sleep(2.5)
Kasutaja1.kirjelda_kasutajat()
time.sleep(2)
print("Tere " + nimi + "!")
time.sleep(1.5)
