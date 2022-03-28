# 6▹ Wywołaj błąd związany z otwarciem pliku.
#
# Spróbuj odczytać plik, który nie istnieje.
#
# Spróbuj odczytać wartość z pliku otwartym w trybie w
#
# Spróbuj utworzyć plik, który już istnieje w trybie x
#
# Obsłuż w dowolny sposób każdy z powyższych błędów.
import io

try:

    with open(filename,"r",encoding="utf-8") as f:
        f.readlines()

    with open("cos.txt","r",encoding="utf-8") as f:
        f.readlines()


    with open("error.txt","w",encoding="utf-8") as f:
        f.readlines()


    with open("error.txt","x",encoding="utf-8") as f:
        f.write("hello world")
except NameError:
    print("Błąd nazwy pliku")
except FileNotFoundError:
    print("Taki plik nie istnieje")
except io.UnsupportedOperation:
    print("NIe da rady")
except FileExistsError:
    print("Taki plik nie istnieje")


'''
NameError
FileNotFoundError
io.UnsupportedOperation
FileExistsError

'''

# inaczej

try:
    with open(filename,"r",encoding="utf-8") as f:
        f.readlines()
except NameError:
    print("Błąd nazwy pliku")

try:
    with open("cos.txt","r",encoding="utf-8") as f:
        f.readlines()
except FileNotFoundError:
    print("Taki plik nie istnieje")

try:
    with open("error.txt","w",encoding="utf-8") as f:
        f.readlines()
except io.UnsupportedOperation:
    print("NIe da rady")

try:
    with open("error.txt","x",encoding="utf-8") as f:
        f.readlines()
except FileExistsError:
    print("Taki plik nie istnieje")


