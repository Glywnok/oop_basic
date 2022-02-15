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
        sit = 0
        while sit == 0:
            if ask == self.password:
                print("Sisestatud parool on õige")
                sit += 1
            else:
                print("Parool on vale")
                self.times += 1
                if self.times == self.sisselogimiskatsed:
                    print("Te olete sisestatud valesti parooli juba " + str(
                        self.times) + " te ei saa rohkem sisestada parooli.")
                    self.times = 0
                    exit()