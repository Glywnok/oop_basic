class Sisselogimine():
    def __init__(self, password, suurenda, sisselogimiskatsed, eesnimi, perenimi):
        self.sisselogimiskatsed = sisselogimiskatsed
        self.suurenda_sisselogimiskatsed = suurenda
        self.password = password
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.times = 0


    def kirjelda_kasutajat(self):
        print("Kasutaja andmed: ")
        print("Kasutaja eesnimi on " + str(self.eesnimi))
        print("Kasutaja perekonnanimi on " + str(self.perenimi))
        print("Kasutaja parool on " + str(self.password))


    def tervitaja_kasutajat(self):
        print("Tere " + str(self.eesnimi) + " " + str(self.perenimi))


    def password_test(self):
        ask = str(input("Sisestage palun sisse oma parooli: "))
        if ask == self.password:
            print("Sisestatud parool on õige")
        else:
            print("Parool on vale")
            self.times += 1
            if self.times == self.sisselogimiskatsed:
                print("Te olete sisestatud valesti parooli juba " + str(self.times) + " te ei saa rohkem sisestada parooli.")
                self.times = 0
                exit()


    def Special_access(self, add_u, delete, chng, add_f, remove, admin):

        adm = ""
        adu = ""
        de = ""
        chn = ""
        adf = ""
        ref = ""
        if add_u == "1":
            adu = " võib lisada teist kasutajat"
        elif add_u == "0":
            adu = " ei või lisada teist kasutajat"
        else:
            print(add_u)
            print("ERROR")

        if delete == "1":
            de = " võib kustutada teist kasutajat"
        elif delete == "0":
            de = " ei või kustutada teist kasutajat"
        else:
            print(delete)
            print("ERROR")

        if chng == "1":
            chn = " võib muutuda teist kasutajat"
        elif chng == "0":
            chn = " ei või muutuda teist kasutajat"
        else:
            print(chng)
            print("ERROR")

        if add_f == "1":
            adf = " võib lisada uut faili"
        elif add_f == "0":
            adf = " ei või lisada uut faili"
        else:
            print(add_f)
            print("ERROR")

        if remove == "1":
            ref = " võib kustutada faili"
        elif remove == "0":
            ref = " ei või kustutada faili"
        else:
            print(remove)
            print("ERROR")

        if admin == "1":
            adm = " kasutaja on admin"
        elif admin == "0":
            adm = " kasutaja pole admin"
        else:
            print(admin)
            print("ERROR")


        print("Kasutaja võib: " + adu + "," + de + "," + chn + "," + adf + "," + ref + "ja " + adm + ".")

    def access(self, add_u, delete, chng, add_f, remove, admin):

        self.add_user = add_u
        self.delete_user = delete
        self.change_user = chng
        self.add_file = add_f
        self.remove_file = remove
        self.admin_user = admin

        if add_u == "1":
            print("Add_User avaible")
        elif add_u == "0":
            print("Add_user not avaible")
        else:
            print(add_u)
            print("ERROR")

        if delete == "1":
            print("Delete user avaible")
        elif delete == "0":
            print("Delete user not avaible")
        else:
            print(delete)
            print("ERROR")

        if chng == "1":
            print("Change user avaible")
        elif chng == "0":
            print("Change user not avaible")
        else:
            print(chng)
            print("ERROR")

        if add_f == "1":
            print("Add file avaible")
        elif add_f == "0":
            print("Add file not avaible")
        else:
            print(add_f)
            print("ERROR")

        if remove == "1":
            print("delete file avaible")
        elif remove == "0":
            print("delete file not avaible")
        else:
            print(remove)
            print("ERROR")

        if admin == "1":
            print("User is Admin")
        elif admin == "0":
            print("User is not admin")
        else:
            print(admin)
            print("ERROR")