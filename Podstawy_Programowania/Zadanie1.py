#zadanie #1
import random
zakresMin = eval(input("Podaj najmiejsza liczbe do losowania: "))
zakresMax = eval(input("Podaj najwieksza liczbe do losowania: "))

licznik = 1
while licznik < 6:
    Losowanie = random.randrange(zakresMin,zakresMax)
    print("Liczba",licznik,": ",Losowanie)
    licznik += 1