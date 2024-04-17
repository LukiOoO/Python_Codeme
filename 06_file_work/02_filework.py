# 2▹ Zapoznaj się z modułem os. Sprawdź rozmiar utworzonego przez siebie pliku.

import os

# rozmiar pliku podany jest w bajtach
def txt_size():
    with open("tekst.txt", 'r',encoding="utf-8") as fopen:
        c = os.path.getsize("tekst.txt")
        print(c)

txt_size()