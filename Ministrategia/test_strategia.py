import unittest
from wojownik import Wojownik, WojownikError
from jednostki.rycerz import Rycerz
from druzyna import Druzyna


class TestWojownik(unittest.TestCase):
    def test_warrior_with_correct_life(self):
        w = Wojownik(30)
        self.assertEqual(w._zycie, 30)
        self.assertEqual(w._doswiadczenie, 0)

    def test_warrior_with_incorrect_life(self):
        with self.assertRaises(WojownikError):
            Wojownik(-100)

    def test_repr(self):
        w = Wojownik(30)
        expected = 'Wojownik: hp=30, exp=0'
        received = w.__repr__()

        self.assertEqual(expected, received)

    def test_marsz(self):
        w = Wojownik(30)
        w.maszeruj(1000)
        self.assertEqual(20.0, w._doswiadczenie)


class TestRycerz(unittest.TestCase):
    def test_atakuj(self):
        r = Rycerz()
        r.atakuj()
        self.assertEqual(0.3, r._doswiadczenie)

    def test_stworzenie_udane(self):
        r = Rycerz()
        self.assertEqual(r._zycie, 60)
        self.assertEqual(r._doswiadczenie, 0)


class TestDruzyna(unittest.TestCase):
    def test_stworzenie(self):
        d = Druzyna()
        self.assertEqual(d.wojownicy, [])

    def test_dodawanie(self):
        d = Druzyna()
        r1 = Rycerz()
        d.dodaj_wojownika(r1)
        self.assertEqual(d.wojownicy, [r1])


if __name__ == '__main__':
    unittest.main()