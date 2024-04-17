# Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce.
# W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.


rating_1 = int(input('Podaj pierwszą ocenę : '))
rating_2 = int(input('Podaj drugą ocenę : '))
rating_3 = int(input('Podaj trzecią ocenę : '))

rating_avg = (rating_1 + rating_2 + rating_3) / 3

if rating_avg > 7:
    print('bardzo dobry')

elif (rating_avg >= 5) and (rating_avg <= 7):
    print('przeciętna')

elif rating_avg <= 4:
    print('nie warta uwagi')