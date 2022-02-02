import time
class Kasutaja():


    def __init__(self, nickname, suurenda, sisselogimiskatsed, password):
        self.nickname = nickname
        self.suurenda_sisselogimiskatsed = suurenda
        self.sisselogimiskatsed = sisselogimiskatsed
        self.times = 0
        self.password = password

    def kirjelda_kasutajat(self):
        print("Kasutaja andmed: ")
        print("Kasutaja: " + self.nickname)
        print("Kasutaja parool on: " + self.password)

    def tervitaja_kasutajat(self):
        print("Tere " + str(self.nickname))

    def password_test(self):
        while self.times <= self.sisselogimiskatsed:
            ask = str(input("Sisestage palun sisse oma parooli: "))
            if ask == self.password:
                print("Sisestatud parool on õige")
                setup = True
                break
            else:
                print("Parool on vale")
                self.times += 1
                if self.times == self.sisselogimiskatsed:
                    print("Te olete sisestatud valesti parooli juba " + str(self.times) + " te ei saa rohkem sisestada parooli.")
                    self.times = 0
                    exit()
                setup = False
        return setup

    def kontroll_password(self, password):
        if len(password) < 6:
            print("Uus parool on liiga lühike. ")
            return False
        else:
            if len(password) > 10:
                print("Uus parool on liiga pikk.")
                return False
            else:
                return True


    def set_password(self, new_password):
        if self.kontroll_password(new_password):
            self.password = new_password

    def NEW_PASS(self, setup):
        if setup == True:
            sit = False
            while sit == 0:
                Password = input("Sisestage palun oma parool: ")
                Password_try = input("Sisestage palun see sama parool: ")
                if Password == Password_try:
                    sit = 1
                    new_password = Password
                else:
                    print("Sisestatud parool on vale, proovige uuesti!")
                    time.sleep(3)
        return new_password



    def get_password(self):
        #print("Teie parool on: " + self.password)
        return self.password
