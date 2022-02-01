class Kasutaja():

    def __init__(self, eesnimi, perenimi):
        self.eesnimi = eesnimi
        self.perenimi = perenimi

    def kirjelda_kasutajat(self):
        print("Kasutaja andmed: ")
        print("Kasutaja eesnimi on " + str(self.eesnimi))
        print("Kasutaja perekonnanimi on " + str(self.perenimi))

    def tervitaja_kasutajat(self):
        print("Tere " + str(self.eesnimi) + " " + str(self.perenimi))


#    def __del__(self):


