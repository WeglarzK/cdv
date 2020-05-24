slownik = {'key1':'value1','key2':'value2'}

'''
    Utwórz słownik o nazwie pracownik zawierający klucze:
    imie, nazwisko,miasto,wiek,imionaDzieci (podaj dwa imiona), imionaRodzicow (podaj dwa imiona rodzicow)

'''

pracownik = {
 'imie': 'Karol',
 'nazwisko':'Nowak',
 'miasto':'Poznan',
 'wiek':'21',
 'imionaDzieci':'[Asia,Malgorzata]',
 'imionaRodzice':'[Stanislaw,Mariola]'
}
print(pracownik)
print(pracownik['imionaDzieci'])
print(pracownik['imionaDzieci'][0])

pracownik['wzrost']=175
pracownik['waga']=80
print(pracownik)

#######################################################


pracownik1 = {
    'name' : 'Anna',
    'surname' : 'Kowalska',
    'city' : 'Poznań',
    'age' : 24
}

print()
print(pracownik1)

key = 'age'
if key in pracownik1:
    del pracownik1[key]
    print(f'Klucz {key} zostal usuniety')
else:
    print(f'Klucz {key} nie został usuniety')

print(pracownik1)

print(pracownik1.keys())
print(pracownik1.values())

print(list(pracownik1.values()))
print(pracownik1.items())

for value in pracownik1.values():
    print(value, end=" ")
print()

for key, value in pracownik1.items():
    print(f'{key}: {value}')

'''
 Utwórz słownik, który zawiera dane podane przez użytkownika z klawiatury: imie, nazwisko, wiek
 przypisz do słownika dane pobrane od dwóch użytkowników
 Wyświetl dane w formacie:
 user1: {imie} {nazwisko} wiek: {wiek}
 user1: {imie} {nazwisko} wiek: {wiek}
 Średni wiek użytkowników wynosi: {sredni wiek} lat
'''
guest1 = {
    'name' : '',
    'surname' : '',
    'age' : 0 }

guest2 = {
    'name' : '',
    'surname' : '',
    'age' : 0 }

guest1['name'] = input('Podaj swoje imie: ')
guest1['surname'] = input('Podaj swoje nazwisko: ')
guest1['age'] = eval(input('Podaj swoj wiek: '))

guest2['name'] = input('Podaj swoje imie: ')
guest2['surname'] = input('Podaj swoje nazwisko: ')
guest2['age'] = eval(input('Podaj swoj wiek: '))

srednia_wieku = (guest1['age'] + guest2['age'])/2

print(guest1['name'])
print()
print(srednia_wieku)