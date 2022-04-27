# 2▹ Napisz kod, który zwraca sumę wszystkich wielokrotności 5 lub 7 poniżej liczby N.


def main(n):
    number_list = []
    x = 1
    while x < n:
        if x % 5 == 0:
            number_list.append(x)
        elif x % 7 == 0:
            number_list.append(x)
        x = x + 1
    print(number_list)


if __name__ == '__main__':
    n = int(input('Podaj liczbe: '))
    main(n)