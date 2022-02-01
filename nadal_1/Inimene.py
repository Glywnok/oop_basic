class Inimene():

    def __init__(self, name, lastname, qualification):
        self.nimi = name
        self.perekonnanimi = lastname
        self.qualikatsioon = qualification


    def tootaja(self):
        print("Tere!\nSee on teie töötaja andmed:")
        print("Teie töötaja nimi on: " + str(self.nimi))
        print("Teie töötaja perekonnanimi on: " + str(self.perekonnanimi))


    def __del__(self):
        print("Kõige head " + str(self.nimi) + " " + str(self.perekonnanimi))

    def test_quality(self):
        if self.qualikatsioon <= 0:
            print("Teie töötaja kvalifikatsioon on vale ja ei nõusta programmi.")
        if self.qualikatsioon > 1:
            print("Teie töötaja kvalifikatsioon on õige, aga programm ei nõusta teda analüseerida.")


    def tutvustus(self):
        print("Tere, minu nimi on " + str(self.nimi) + " " + str(self.perekonnanimi))