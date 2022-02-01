class Restoraan():


    def __init__(self, restoraani_nimi, soogi_tyyp):
        self.restoraani_nimi = restoraani_nimi
        self.soogi_tyyp = soogi_tyyp


    def kirjelda(self):
        print('Kiosk ' + str(self.restoraani_nimi) + ' pakub ' + str(self.soogi_tyyp) + ".")

    def ava(self):
        print('Kiosk on avatud.')

    def kinni(self):
        print("Kiosk on kinni.")



    #Järgmine kood on ülesanne 9 kohta tehtud.

    def teenindatud_kylastajad(self):
        kylastatud = 0
        end = 0

        while end == 0:
            enter = int(input("Tere!\nMitu inimest külastasid?\nP.S. Kui sisestate numbrit 0 või vähem kui 0 siis see lõppeb"))
            if int(enter) > 0:
                kylastatud = kylastatud + int(enter)
                print("Uus inimeste arv mis külastasid " + self.restoraani_nimi + " on " + str(kylastatud)  + ", arv suurenes " + str(enter) + " võrra.")
            if int(enter) <= 0:
                end = end + 1


class Jaatisekiosk(Restoraan):
    def maara_jaatise_valik(self):
        self.jaatise_valik = []
        print("Lisa jäätise variandid: ")
        while(True):
            valik = input("")
            if valik == "":
                break
            self.jaatise_valik.append(valik)

    def Jaatise_valik(self):
        for nr in range(1, len(self.jaatise_valik) + 1):
            print("(0), (1)".format(nr, self.fjaatise_valik(nr-1)))


