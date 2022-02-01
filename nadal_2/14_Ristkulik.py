from random import randint

class Ristkylik:
    def __init__(self, l, k, m):
        self.laius = int(l)
        self.korgus = int(k)
        self.symbol = str(m)

    def __str__(self):
        ruutu_read = []
        for rea_number in range(self.korgus):
            rida = (self.symbol * self.laius)
            ruutu_read.append(rida)
        ruutu_read = "\n".join(ruutu_read)
        return ruutu_read


    def __add__(self, other):
        #Self is the forst one, and other is the second one
        laius = self.laius + other.laius
        korgus = self.korgus + other.korgus
        symbol_valik = randint(1, 2)
        if symbol_valik == 1:
            symbol = other.symbol
        elif symbol_valik == 2:
            symbol = self.symbol
        uus_ristkylik = self.__init__(self, laius, korgus, symbol)
        print(uus_ristkylik)
        return self


ask1 = input("first laius")
ask2 = input("first korgus")
ask3 = input("mark")
esimene = Ristkylik(ask1, ask2, ask3)
print(esimene)

ask21 = input("second laius")
ask22 = input("second korgus")
ask23 = input("mark")
second = Ristkylik(ask21, ask22, ask23)
print(second)

esimene.__add__(second)


