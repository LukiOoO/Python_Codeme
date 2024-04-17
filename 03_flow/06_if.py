# Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.

x = int(input("Zgadnij liczbę od 1 do 100: "))

secret_number = 50

if x == secret_number:
    print("gratulacj!!")
else:
    print("pudło :(")
