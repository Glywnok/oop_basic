class Kasutaja():

    def __init__(self, eesnimi, perenimi, suurenda, sisselogimiskatsed, password):
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.suurenda_sisselogimiskatsed = suurenda
        self.sisselogimiskatsed = sisselogimiskatsed
        self.times = 0
        self.password = password

    def kirjelda_kasutajat(self):
        print("Kasutaja andmed: ")
        print("Kasutaja eesnimi on " + str(self.eesnimi))
        print("Kasutaja perekonnanimi on " + str(self.perenimi))

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
                print("Te olete sisestatud valesti parooli juba " + str(
                    self.times) + " te ei saa rohkem sisestada parooli.")
                self.times = 0
                exit()

    def setter(self):
        muuda = str(input("Te sisestasite õigesti parooli! Kas te tahate teda muutuda? jah/ei"))
        if muuda == "jah" or "Jah":
            password = str(input("Sisestage oma parooli"))
        return password

    def getter(self):
