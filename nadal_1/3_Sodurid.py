from nadal_1.sodur import Sodur
from random import randint

sodur1 = Sodur()
sodur2 = Sodur()

i = 0
while i < 1:
    dealt = randint(5, 20)
    who = input("Sisestage palun kes rünnab: \nP.S. palun kirjutage kas 1 või 2: ")
    print(dealt)
    if who == ("1"):
        sodur2.hp = sodur2.hp - dealt
        print("Sõdur 2 hp on " + str(sodur2.hp))
        if sodur2.hp <= 0:
            print("Sõdur 2 kaotas, sõdur 1 võitis!")
    if who == 2:
        sodur1.hp = sodur1.hp - dealt
        print("Sõdur 1 hp on " + str(sodur1.hp))
        if sodur1.hp <= 0:
            print("Sõdur 1 kaotas, sõdur 2 võitis!")
