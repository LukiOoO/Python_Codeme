# 5▹ Stwórz grę ciepło zimno.
#
# Komputer losuje liczbę z zakresu od 1 do 100.
#
# Użytkownik podaje swój traf.
#
# Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
#
# Jeśli użytkownik zgadnie wygrywa gracz.
#
# Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.


import random

print("Gra ciepło zimno zgadnij liczbe od 1 do 100 ")

x = random.randint(1, 100)
# print(x)
i = 0

u = int(input("Podaj liczbe rund: "))
y = int(input("Podaj liczbe od 1 do 100: "))
if abs(y - x) <= 15:
    print("Ciepło")
else:
    print("Zimno")

if y == x:
    i += 1
    print("Brawo odgadłeś za",i,"razem")
i = 0




while x != y:

    previus = y
    i += 1
    y = int(input("Podaj liczbe od 1 do 100: "))
    if y == x:
        i += 1
        print("Świetnie wygrałeś za,", i ,"razem")
        break



    diff1 = abs(y - x)
    diff2 = abs(previus - x)
    if diff1 <= diff2:
        print("Ciepło")
    if diff2 <= diff1:
        print("Zimno")

    elif i == u - 1:
        print("koniec przegrałeś :(")
        break




























