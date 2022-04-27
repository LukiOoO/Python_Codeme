def rectangle(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError('Bok musi być wartością numeryczną!')

    return a * b


def triangle(a, h):
    return 0.5 * a * h


def main():
    print(f'Wynik {rectangle(4, 6)}')
    print(f'Wynik {rectangle(4, "B")}')


if __name__ == '__main__':
    main()