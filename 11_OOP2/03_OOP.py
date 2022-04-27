# 3▹ Zadanie inspirowane popkulturą: https://www.youtube.com/watch?v=Ct6BUPvE2sM
#
# Stwórz klasę PenPinapple, która dziedziczy z klas Pen oraz Pinapple. Logiki to nie ma, więc dodaj wg uznania.

class pen():

    def pen(self):
        print("I have pen")

class pinapple():

    def pinapple(self):
        print("I have pinapple")


class pinapplepen(pen, pinapple):
    def pinapplepen(self):
        print("Pinapplepen ")


pinapplepen1 = pinapplepen().pen()
pinapplepen2 = pinapplepen().pinapple()
pinapplepen3 = pinapplepen().pinapplepen()