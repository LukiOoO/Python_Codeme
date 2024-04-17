# Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.


x = int(input("Podaj pierwszą liczbe całkowitą: "))

y = int(input("Podaj drugą liczbę całkowitą: "))

z = x + y

if z > 100:
    print(f"Wynikiem dodania jest: {z}")
else:
    print("Koniec")