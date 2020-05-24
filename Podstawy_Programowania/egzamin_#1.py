
print("Podaj liczbę a: ")
a = float(input())
print("Podaj liczbe b: ")
b = float(input())
print("Podaj liczbe c: ")
c = float(input())



if (a-b != 0):
    if c>0:
        print("Wartosc wyrazenia wynosi: ")
        print((a**2)+b)
    if c<0:
        print("Wartosc wyrazenia wynosi: ")
        print(a-(b**2))
    if c==0:
        print("Wartosc wyrazenia wynosi: ")
        print(1/(a-b))
else:
    print("Proba dzielenia przez 0")




