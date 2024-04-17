# Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8).
#


x = int(input("Podaj liczbe < 8 : "))
silnia = 1

if x <= 8:
    for x in range(2,x + 1):
        silnia = silnia * x
    print(silnia)
else:
    print("liczba musi byc <= 8")
