"""Moodul sisaldab andmete jagamine õigele õpilasele, ehk mida ta õpib"""
class Andmed:
    def __init__(self, *info):
        """Siit saame kõiki ained mida õpetaja õpetab"""
        self.info = list(info)
    def __getitem__(self, i):
        """Siin kood võtab ainult õige aine mdia õpilane õpetab""""\n"""""Plaun vaadata "main.py" number 1.A"""
        return self.info[i]

