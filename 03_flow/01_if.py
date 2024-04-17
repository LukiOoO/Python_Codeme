#1. Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.



number = int(input("podaj liczbe: "))
# number = input("Podaj liczbe 1-100: ")
# number = int(number)

if number % 3 == 0:
    print(f"liczba {number} jest podzielna przez 3 bez reszy")
else:
    print(f"liczba {number} nie jest podzielna przez 3 bez reszy")