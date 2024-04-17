# 3▹ Stwórz listę 10 elementową (różne typy!).
# Pozwól użytkownikowi podać dowolny index.
# Podziel 1 przez liczbę pod indexem wybranym przez użytkownika. Obsłuż błędy.

elem = [0, 2.5, {'wartosc': 3}, 'ygii', [2, 1], 13, "string", 2.45, 0, ('1', '2'), [], {1,2}, {'klucz': 123}, range(10)]

try:
    user = int(input('Podaj index'))
    user_elem = elem[user]
    print(user_elem)
    1 / user_elem
except (TypeError, IndexError) as e:
    print('Nie da rady')
except ValueError:
    print('LOL, to nie jest dobra wartość')
except ZeroDivisionError:
    print('Pamiętaj... nie dziel przez zero!')