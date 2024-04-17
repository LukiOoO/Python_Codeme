# 5.Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej
# 1 dużą literę i mieć długość conajmniej 8 znaków. Poinformuj użytkownika,
# jeśli wpisane hasło jest nie poprawne. Wyświetl różne komunikaty w zależności od rodzaju błędu.




password = input("Podaj Hasło: ")

if len(password) < 8:
    print("Hasło jest za krótkie musi mieć min. 8 znaków")
elif password.isalpha() or password.isdigit():
    print("Haslo musi zawierać zarówno cyfry i litery")
elif password.islower():
    print("Hasło musi zawierać conajmniej 1 dużą litere")
elif password.isupper():
    print("Hasło musi zawierać conajmniej 1 małą litere")
else:
    print("Twoje hasło jest prawidłowe")
