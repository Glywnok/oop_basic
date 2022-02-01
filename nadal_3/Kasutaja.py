class Kasutaja():

    def __init__(self, kasutaja):
        self.kasutaja = kasutaja
        #self.nimi = nimi
#        self.perenimi = perenimi
        self.password = "qwerty"

    def kirjelda_kasutajat(self):
        print("Kasutaja andmed: ")
        print("Kasutaja: " + str(self.kasutaja))
        print("Kasutaja parool: " + str(self.password))


#  def tervitaja_kasutajat(self):
#     print("Tere " + str(self.eesnimi) + " " + str(self.perenimi))


    def setter(self, setter):
        self.password = setter

    def getter(self):
        print("parool on: " + str(self.password))

    #def