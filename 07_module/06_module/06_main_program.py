# 6▹ Stwórz program, który dla dowolnego ciągu znajduje najdłuższą sekwencję takich samych znaków oraz jej długość np.
#
# Wejście:
# var = ‘banannnnannnnnnnnnanananananaaaana’
#
# Wyjście
# ‘nnnnnnnnn’, 9
#
# Utwórz generator instancji testowych, który wygeneruje losowe ciągi znaków składające się z jedynie z cyfr o
# d 0-9. Upewnij się, że conajmniej 2 takie same znaki znajdą się w sekwencji.
#
# Zmodyfikuj generator tak, by oczekiwał znaków podanych przez użytkownika np. użytkownik podaje 4 znaki: ‘a’, ‘b’, ‘c’, ‘*’.
#
# Zaimportuj generator bezpośrednio do programu.
from generator import instance_generator as ig

def sequence(x):
    user_string = x
    low = 0
    up = 1
    flow = 0
    fup = 1
    while up < len(user_string):
        if user_string[up] != user_string[up - 1]:
            if fup - flow < up - low:
                flow, fup = low, up
            low = up
        up += 1
    if fup - flow < up - low:
        flow, fup = low, up
    return print("Najdłuższy ciąg takich samych znaków w kodzie to: ",user_string[flow:fup])


def main():
    x = ig()
    print(x)
    sequence(x)







if __name__ == "__main__":
    main()


