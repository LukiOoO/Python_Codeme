def circle_area():
    r = float(input('Podaj promień ->'))
    pi = 3.14
    print('Pole: ', pi * (r**2))


def square_area():
    a = float(input('Podaj bok kwadratu ->'))
    print('Pole: ', a*a)

def main():
    # ---- main ---
    print('ZAIMPORTOWANO !')
#
# if __name__ == '__main__':
#     print('if się wykonał')
#     main()

print(__name__)
