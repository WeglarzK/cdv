programowanie=['Python','PHP','C#','JS', 'Java']
print(programowanie)
print(type(programowanie))

first=programowanie[0]
print(first)

threeElements = programowanie[0:3]
print(threeElements)

lastElement = programowanie[-1]
print(lastElement)

#Dodawanie nowego elementu na koniec listy
programowanie.append('R')
programowanie.append('Python')
print(programowanie)

#zliczanie elementów listy
count = programowanie.count('Python')
print(count)

#ilość elementów w liście
countElementsOfList = len(programowanie)
print(countElementsOfList)

#połączanie list
anotherList=['C','C++']
programowanie.extend(anotherList)
print(programowanie)
