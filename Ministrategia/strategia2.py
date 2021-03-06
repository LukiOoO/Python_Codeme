class Rycerz:
    def __init__(self):
        self._zycie = 60
        self._doswiadczenie = 0

    def __repr__(self):
        return f'Rycerz: hp={self._zycie}, exp={self._doswiadczenie}'

    def maszeruj(self, dystans):
        print(f'Rycerz: Przeszedłem {dystans}m')
        self._doswiadczenie += 0.02 * dystans

    def atakuj(self):
        print('Rycerz: Machnąłem mieczem!')
        self._doswiadczenie += 0.3


class Lucznik:
    def __init__(self):
        self._zycie = 40
        self._doswiadczenie = 0

    def __repr__(self):
        return f'Łucznik: hp={self._zycie}, exp={self._doswiadczenie}'

    def maszeruj(self, dystans):
        print(f'Łucznik: Przeszedłem {dystans}m')
        self._doswiadczenie += 0.02 * dystans

    def atakuj(self):
        print('Łucznik: Wypuściłem strzałę!')
        self._doswiadczenie += 0.4

def main():
    p = Rycerz()
    print(p)
    p.maszeruj(10)
    print(p)
    p.atakuj()
    print(p)

    l = Lucznik()
    print(l)
    l.maszeruj(15)
    print(l)
    l.atakuj()
    print(l)

if __name__ == '__main__':
    main()