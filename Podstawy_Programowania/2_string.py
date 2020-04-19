text = "Anna, paweł, TomEK"

'''
komentarz
blokowy
'''

#Rozdzielanie tablicy
tab = text.split(", ")
print(text)

print(tab)
print(type(tab))
name1=tab[0]
print("Twoje imie: " + name1)

#Zamiana na duże litery
nameUpper = name1.upper()
print(nameUpper)

#Zamiana na małe litery
nameLower = name1.lower()
print(nameLower)

'''
#Sprawdzenie zawartości
surname = input()
content = surname.isalpha()
print(content)
print(type(content))
'''

name = "Katarzyna"
print("\nDane uzytkownika\nMasz na imie: ", name)

text1="Jan\n"
text2="Nowak"
print(text1 + text2)

#Usuwanie białych znaków na końcu stringa
text1=text1.rstrip()
print(text1 + text2)
print(text1 + " " + text2)

#wyświetlenie łańcuchów znaków

#wszystkie wersje Pythona
text = "%s, Java i %s" % ("PHP" , "Python")
print(text)

#nowsze wersje Python > 2.6
text = "{1}, Java i {0}".format("PHP", 'Python')
print(text)

#Jak korzystać z help'a
#help(text.replace)

#Zamiana fragmentu tekstu
new = text.replace("PHP", "C#")
print(new)

#Wypisanie danych
year = 2020
month = "April"
day = 19

print("Data: ", end="")
print(day, month, year)

#Drugi sposób (zmiana separatora)
print(day, month, year, sep="-")
