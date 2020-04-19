#pi
import math
pi = math.pi
print(pi)

#pierwiastek
element = math.sqrt(9)
print(element)

#moduł random
import random
losuj = random.random()
print(losuj)

#losowanie z listy

randomOfList = random.choice([1 ,2 ,33 ,4 ,15 ])
print(randomOfList)

#zadanie #1

zakresMin = eval(input("Podaj najmiejsza liczbe do losowania: "))
zakresMax = eval(input("Podaj najwieksza liczbe do losowania: "))

licznik = 1
while licznik < 6:
    Losowanie = random.randrange(zakresMin,zakresMax)
    print("Liczba",licznik,": ",Losowanie)
    licznik += 1





















