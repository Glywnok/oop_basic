from nadal_3.Kasutaja import Kasutaja


Kasutaja1_name = input("Sisestage palun oma kasutaja nimet: ")

Kasutaja1 = Kasutaja(Kasutaja1_name)

password = input("Kas sa tahad muuda oma parooli? \nKui jah siis siestage uut praooli \n")
if password == "":
    print("")
else:
    Kasutaja1.setter(password)

print(Kasutaja1.getter())