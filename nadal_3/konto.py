class Konto:
    # kirjeldab panga kontot

    def __init__(self, nimi, saldo):
        self.nimi = nimi
        self.saldo = saldo

    def ylekanne(self, kogus):
        self.saldo = self.saldo - kogus

    def deposiit(self, kogus):
        self.saldo = self.saldo + kogus

    def naita_saldo(self):
        return str(self.saldo) + " €"

    def naita_nimi(self):
        return "Teie kasutaja nimi on: " + self.nimi