def zadanie2():
  wielkosc = int(input("Wprowadź liczbę elementów do posortowania <1 .. 10>: "))
  while( 10 < wielkosc or wielkosc < 1 ):
    print("Zła liczba, spróbuj ponownie ...")
    wielkosc = int(input("Wprowadź liczbę elementów do posortowania <1 .. 10>: "))
  arr = []
  for i in range(int(wielkosc)):
    arr.append(int(input("Wprowadź liczbę [%s]=" % str(i+1))))
  arr = sorted(arr)
  print("Wyprowadzanie posortowanych elementów:")
  for i in range(int(wielkosc)):
    print("Element [%s]=%s" % (str(i+1), str(arr[i])))

zadanie2()