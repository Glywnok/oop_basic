from Inimesed import *

teemad = Andmed("klass", "objekt", "pärilus", "polümorfism", "kalseldus")
a = True
while a == True:
    ask_teemad = input("Sisestage sisse teemasid mida õpetaja õpetab")


anna = Õpeataja()
mati = Õpilane()
raul = Õpilane()

anna.õpetab(teemad[4], raul, mati)
anna.õpetab(teemad[2], raul)

print(raul.teadmised)
print(mati.teadmised)


'''
from Inimesed import *



teemad = Andmed("klass", "objekt", "pärilus", "polümorfism", "kalseldus")
a = True
while a == True:
    ask_teemad = input("Sisestage sisse teemasid mida õpetaja õpetab")
    if ask_teemad == "":
        break
        a = False
    else:
        teemad.append(ask_teemad)


Teacher = Õpeataja()
mati = Õpilane()
raul = Õpilane()
a = True
while a == True:
    student = input("Keda Õpetaja õpetab? Kas Mati või Rauli? ")
    if student == "":
        break
        a = False
    i = int(input("Mida teema õpetaja õpetab? \nP.S. Võite sisestada 1 - 5"))
    i -= 1
    Teacher.õpetab(teemad[int(i)], student.lower)
'''
