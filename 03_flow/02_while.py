# ) Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5). Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_number = 5


x = int(input("podaj liczbe od 1 do 20: "))

while x != secret_number:
    x = int(input("podaj liczbe od 1 do 20: "))
    if x > secret_number:
        print()
    elif x < secret_number:
        print()

print("brawo wygrałeś")