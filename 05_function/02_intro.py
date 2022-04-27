# 2▹ Napisać funkcję, która sprawdza czy liczba jest parzysta.

def even_number(number):
    if number % 2 == 0:
        print("Liczba jest parzysta ")
    else:
        print("Liczba jest nie parzytsa")



user_number = int(input("Podaj liczbę: "))


even_number(user_number)