print("CDV111")
print(8)

#potęgowanie
pow = 2 ** 10
print(pow)

text = "CDV"
print(text * 2)

#pobieranie danych z klawiatury
#  + konkatenacja
name = input()
print("Twoje imie: " + name)

surname=input()
print("Twoje imie: " + name + ", nazwisko: " + surname)

length = len(surname)
print(length)
print(type(surname))
print(type(length))

length = str(length)
print(type(length))

'''
Użytkownik podaje z klawiatury swoje dane: imie, nazwisko, wiek,
wyświetl dane w formacie: 
Imie i nazwisko: ..., wiek: ... lat
'''

print("\nPodaj swój wiek:", end="")
surname="Kowalski"
firstLetter = surname[0]

lastLetter = surname[len(surname) -1]
print(lastLetter)

#konwersja
x = "5"
print(type(x))
x = int(x)
print(type(x))

y = 4
print(type(y)) #int
y = y / 2
print(type(y)) #float
print(y) #2.0

surname = "Kowalski"
print()
print(surname[0]) #K
print(surname[0:3]) #Kow
print(surname[-2]) #k
print(surname[-2:]) #ki
print(surname[:-2]) #Kowals
print(surname[:-2:2]) #Kwl

print()