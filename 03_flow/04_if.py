# Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.


# signs = "asdasdscaADASDAdasda"
signs = str(input("podaj ciąg znaków: "))

if "a" in signs:
    print(signs.replace("a","z"))
else:
    print()

if len(signs) > 5:
    print("ciąg ma więcej niż 5 znaków")
else:
    print()
