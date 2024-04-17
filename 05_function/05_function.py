# 5▹ Napisz grę ciepło - zimno tak, aby korzystać z funkcji.

import random


def main_mechanic(y,u):
    x = random.randint(1, 100)
    i = 0
    if abs(y - x) <= 15:
        print("Ciepło")
    else:
        print("Zimno")

    if y == x:
        i += 1
        print("Brawo odgadłeś za", i, "razem")
    i = 0

    while x != y:

        previus = y
        i += 1
        y = int(input("Podaj liczbe od 1 do 100: "))
        if y == x:
            i += 1
            print("Świetnie wygrałeś za,", i, "razem")
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









print("Gra ciepło zimno zgadnij liczbe od 1 do 100 ")

u = int(input("Podaj liczbe rund: "))
y = int(input("Podaj liczbe od 1 do 100: "))

main_mechanic(y,u)