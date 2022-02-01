from nadal_3.Kasutaja import Kasutaja
password = "qwerty"
nimi = str(input(("Tere!\n Palun sisestage oma nimet: ")))
perenimi = str(input("Sisestage oma perekonna nimet: "))

print("Teie paroolon juba määratud, kui te tahate teda muuta palun sisestage järgmised andmed: ")

katsed_suurendamine = int(input("On võimalik, et te ei mäleta oma parooli, ja te tahate suurendada parooli sisselogimis katseid: siis kui palju te tahate et see arv suurenes? "))
katsed = int(input("Maksimaalne arv katse: "))

Kasutaja1 = Kasutaja(nimi, perenimi, katsed_suurendamine, katsed, password)

Kasutaja1.password_test()
print(password)

Kasutaja2 = Kasutaja(nimi, perenimi, katsed_suurendamine, katsed, password)

