def check_values(*values):
    for i in values:
        if not isinstance(i, (int, float)):
            raise ValueError(f'Bok {i} musi być wartością numeryczną!')


def rectangle(a, b):
    check_values(a, b)
    return a * b


def triangle(a, h):
    check_values(a, h)
    return 0.5 * a * h


def trapezoid(a, b,  h):
    check_values(a, b, h)
    return 0.5 * (a + b) * h



def main():
    print(rectangle(4, 6))
    print(trapezoid(4, 3, 6))
    #print(rectangle(4, 'aaa'))
    #print(trapezoid(4, 3, 'aaa'))


if __name__ == '__main__':
    main()