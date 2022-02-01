class Inimene():
    jk = 0
    def __init__(self):
        self.id = Inimene.jk + 1
        Inimene.jk += 1
    def info(self):
        print("id = {0}".format(self.id))