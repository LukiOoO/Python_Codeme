# 4▹ Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”
# , “nie, liczba x jest z poza zakresu”.


def cheack_number(number_ragne,user_number):
    if user_number in number_ragne:
        print("liczba", user_number, "znajduje się w zakresie")
    else:
        print("liczba", user_number, "nie znajduje się w zakresie")

def user_number_range():
    list_number = []
    for x in range(0,101):
        list_number.append(x)

    user_number = int(input("Podaj liczbe aby sprawdzic czy jest w zakresie: "))
    cheack_number(list_number,user_number)

user_number_range()


