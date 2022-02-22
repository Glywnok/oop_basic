"""See moodul deklaleerib mida õpetaja õpetab ja mida õpilane õpib."""
from Andmed import Andmed

class Õpeataja:
    """Siin klassis kood võtab kõiki mida õpetaja õpetab ja paneb teda Andmesse"""
    def õpetab(self, info, *õpilane):
        for i in õpilane:
            i.õpib(info)

class Õpilane:
    """Siin klassis kood võtab teema mida õpilane õpib ja paneb teda listi kus ta jääb, ja kui õpilane akkab õppima uue teema siis ta paneb ka sinna listi"""
    def __init__(self):
        #self.nimi = nimi
        self.teadmised = []
    def õpib(self, info):
        """Siin kood võtab teema ja paneb seda teemat listi sisse"""
        self.teadmised.append(info)
        #print("Nüüd " + self.nimi + " õppib " + info + " .")