# 4▹ Oblicz średnią arymetyczną z kilku liczb. Liczby będą podane przez użytkownika po przecinku.
# Napisz funkcję, która przyjmie wartości i wyświetli średnią. Program powinen być odporny na błędy użytkownika.
# Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.
#
import logging


def average_of_numbers():

    while True:
        try:
            number_user = input("Podaj liczby po przecinku: ")
            x = number_user.split(",")
            y = [int(i) for i in x]
            av = sum(y) / len(y)
            print("Średnia liczb które podałeś to ---> ",av)
            break
        except(ValueError):
            print("Wystąpił błąd ")
            with open("error.txt","a+",encoding="utf-8") as r:
                r.write("Value Error\n")



def main():
    average_of_numbers()


if __name__ == "__main__":
    main()


'''
Value error

'''

