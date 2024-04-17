# 1▹ Utwórz plik na pulpicie zawierający listę ok. 20 cytatów. Każdy cytat powinen się znaleźć w nowej linii. Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś. Np. można wyświetlić tak:
#
# Quote of the day is:
#
# **************************************
#            be or not to be?
# **************************************
# zmodyfikuj plik źródłowy, tak aby użytkownik mógł podać własną nazwę pliku z cytatami
#
# plik z cytatami powinen również zawierać informację o autorze, wyświetl cytat i pod spodem autora
import random

import random


def read_file():
    with open('cytaty.txt',encoding="utf-8") as fopen:
        quotes = fopen.readlines()
    return quotes


def show(quotes):

    quote = random.choice(quotes).strip()
    quote = quote.split(' - ')
    width = len(quote[0]) * 2

    print('Quote of the day: \n')
    print(width * '*')
    print(quote[0].center(width))
    print(quote[1].rjust(width))
    print(width * '*')



quotes_arr = read_file()
show(quotes_arr)