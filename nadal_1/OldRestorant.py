class Restorant():


    def Restorant(self, restoraani_nimi, soogi_tyyp):
        self.restoraani_nimi = restoraani_nimi
        self.soogi_tyyp = soogi_tyyp


    def kirjelda(self):
        print('Restoraan ' + str(self.restoraani_nimi) + ' pakub ' + str(self.soogi_tyyp) + ".")

    def ava(self):
        print('Restoraan on avatud.')

    def kinni(self):
        print("Restoraan on kinni.")