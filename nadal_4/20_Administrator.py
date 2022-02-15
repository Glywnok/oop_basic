from nadal_4.aboba import Sisselogimine
from nadal_4.lesion import Privileegid

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

print("Palun vastata 1 - kui jah, ja 0 - kui ei\n")
Create_user = input("Kas te tahate, et see kasutaja võiks teha uut kasutajat? ")
Delete_user = input("Kas te tahate, et see kasutaja võiks kustutada teist kasutajat? ")
Edit_user = input("Kas te tahate, et see kasutaja võiks muutuda teise kasutaja võimalust? Kui jah siis te peate veel lisada, et kasutaja oleks admin.")
Add_file = input("Kas te tahate, et see kasutaja võiks teha uut faili? ")
Remove_file = input("Kas te tahate, et see kasutaja võiks kustutada failit? ")
Admin =  input("Kas te tahate, et see kasutaja oli ADMIN? ")

if Edit_user == 1:
    if Admin == 0:
        print("Teie kasutaja ei saa muutuda teist kasutajate võimalust")
        Edit_user = 0



Kasutaja_access = Privileegid(Create_user, Delete_user, Edit_user, Add_file, Remove_file, Admin)
print("\n")
Kasutaja_access.privileegid()
print("\n")
Kasutaja_access.access()