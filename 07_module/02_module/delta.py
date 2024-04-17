# 2▹ Stwórz moduł, który przechowuje wzór na deltę. Skorzystaj z wbudowanego modułu math. W nowym pliku wykorzystaj moduł.

import math


'''

delta = b**2 - 4ac

'''


def main():
    while True:
        try:
            a = int(input("Podaj a:"))
            b = int(input("Podaj b: "))
            c = int(input("Podaj c: "))

            delta = (b**2) - (4*a*c)
            print(delta)
            print("Pierwiastek z delty wynosi --> ", math.sqrt(delta))
            break
        except ValueError:
            print("delta jest mniesza od zera podaj wartosci jeszcze raz")

if __name__ == "__main__":
    main()