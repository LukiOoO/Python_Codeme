# 4▹ Wyświetl 3 losowe cytaty

import random

def read_file():
    with open("cytaty.txt",encoding="utf-8") as fopen:
        quotes = fopen.readlines()
    return quotes

def show_3_qutes(quotes):
    quote = random.choices(quotes,weights=[1, 1, 1, 1], k=3)
    print(*quote, end="\n")

x = read_file()
show_3_qutes(x)