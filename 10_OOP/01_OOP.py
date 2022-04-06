# 1▹ Skorzystaj z wprowadzenia do OOP. Stwórz klasę Pies, która posiada wspomniane atrybuty oraz metodę.
#
# atrybuty: imię, kolor sierści, rasę
#
# metody: szczekaj, machaj ogonem
#
# Utwórz kilka obiektów klasy Pies z różnymi parametrami.

class dog():
    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed

    def bark(self, number=1):
        return 'HOW' * number

    def wave_tail(self):
        return 'machu machu'

dyzio = dog('dyzio', 'black', 'mix terrie')
print(dyzio.__dict__)

print(dyzio.bark(10))
print(dyzio.wave_tail())

reksio = dog('reksio', 'white', 'Bielsko-Biała\'dog')
print(reksio.__dict__)