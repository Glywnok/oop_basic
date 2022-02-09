import time
from nadal_3.raamat import raamat

class raamatupood():
    amount_of_rammat = 0
    def __init__(self, nimi, reiting):
        self.raamatupoodinimi = nimi
        self.raamtupoodi_rating = reiting
        self.raamatudelist = []

    def saan_lisada_raamat(self, raamat):

        print("Kas te tahate lisada:\n" + raamat.pealkiri + "\n" + raamat.autor + "\nMis maksab " + raamat.hind + " € \nMillise reiting on " + raamat.reiting + "punkti 10.")


    def lisa_raamat(self, raamat):
        self.raamatudelist.append(raamat)
        raamatupood.amount_of_raamat += 1

    def saan_eemaldada_raamat(self, raamat):
        i = 0
        for raamatud in self.raamatudelist:
            print("Te saate eemalda " + self.raamatudelist[i] + "\n")
            time.sleep(1)
            i += 4
            list_max = self.get_amount(self.raamatudelist)
            if i >= list_max:
                break
        print("\nNeid raamatuid te saate eemalda.")


    def get_amount(self, list):
        count = 0
        for elemnt in list:
            count += 1
        return count

    def eemalda_raamat(self, brooklyn):
        number = input(int("Millest raamatu te tahate eemalda?"))
        x = True
        i = 0
        while x == True:
            print(self.raamatudelist[i])
            i =+ 4
            if self.raamatudelist[i] == "":
                x = False
                raamatupood.amount_of_rammat -= 1
                break



    def naita_koik_raamatud(self):
        print("Raamatukogus on:")
        i = 0
        x = True
        while x == True:
            print(self.raamatudelist[i])
            i += 1
            print("Mida kirjutas " + self.raamatudelist[i])
            i += 1
            print("Raamat maksab " + self.raamatudelist[i])
            i += 1
            print("Milline reiting on " + self.raamatudelist[i])

            if self.raamatudelist[i] == "":
                print("stop?")
                x = False
                break



    def naita_raamatud_hinna_jargi(self):
        pass

    def naita_koige_populaarsem_raamat(self):
        pass


minu_raamat = raamat('naksitralid', 'raud', '10', '8.5')
pood = raamatupood('minu pood', 10)
pood.saan_lisada_raamat(minu_raamat)
