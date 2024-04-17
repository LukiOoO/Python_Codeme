# 1▹ Znajdź największa wspólny dzielnik (NWD) dwóch liczby. Wykorzystaj algorytm Euklidesa.

def main(a,b):
    while a != b:
        if a > b:
            a = a - b
        if a < b:
            b = b - a
    return a


if __name__ == '__main__':
    a = int(input('Podaj liczbę a : '))
    b = int(input('Podaj liczbę b : '))
    print('NWD:', main(a,b))