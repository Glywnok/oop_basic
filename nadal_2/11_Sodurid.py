from random import randint
from nadal_2.NewInimesed import Sodur



army_1 = []
army_2 = []

for kord in range(20):
    army = randint(1, 2)
    sodur = Sodur(army)
    if army == 1:
        army_1.append(sodur)
    elif army == 2:
        army_2.append(sodur)
    else:
        print("ERROR!")

print("Armee 1: ")
for sodur in army_1:
    sodur.info()
print("-----------------")
print("Armee 2: ")
for sodur in army_2:
    sodur.info()


