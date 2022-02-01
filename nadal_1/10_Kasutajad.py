from nadal_1.Sisselogimine import Sisselogimine

sit = False
while sit == 0:
    Kasutaja1_password = input("Sisestage palun oma parool: ")
    Kasutaja1_password_try = input("Sisestage palun see sama parool: ")
    if Kasutaja1_password == Kasutaja1_password_try:
        sit = 1

password_try = int(input("Mitu korda te tahate et võiks sisestada parooli? P.S. Max tries "))
password_try_plus = int(input("On võimalik, et te ei mäleta oma parooli, ja te tahate suurendada\n parooli sisselogimis katseid: siis kui palju te tahate et see arv suurenes? "))

Kasutaja_nimi = str(input("Palun sisestage oma kasutaja nimet: "))
Kasutaja_perenimi = str(input("Palun sisestage oma perekonnanimet: "))

Kasutaja1 = Sisselogimine(Kasutaja1_password, password_try, password_try_plus, Kasutaja_nimi, Kasutaja_perenimi)
Kasutaja1.kirjelda_kasutajat()
Kasutaja1.password_test()