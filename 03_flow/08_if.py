# Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych. Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.
x = int(input("Podaj 1 liczbę : "))
y = int(input("Podaj 2 liczbę : "))
z = int(input("Podaj 3 liczbę : "))

if (x > y) and (x > z):
    maxim = x
elif (y > x) and (y > z):
    maxim = y
else:
    maxim = z


if x < y:
    temp = x
    x = y
    y = temp
if x < z:
    temp = x
    x = z
    z = temp
if y < z:
    temp = y
    y = z
    z = temp
    print(x, y, z)

