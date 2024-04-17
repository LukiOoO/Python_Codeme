# 2▹ Utwórz klasę dla storczyków. Storczyki z zasady mają różne kolory
# , pory kwitnienia, gatunki. Utwórz dowolne atrybuty i metody. Dodaj atrybut wspólny dla
# wszystkich storczyków - królestwo roślin.
#
# Utwórz kilka storczyków z różnymi parametrami.


class orchid():
    def __init__(self,color,flowering_seasons,species):
        self.color = color
        self.flowering_seasons = flowering_seasons
        self.species = species

    def germination(self,time=5):
        print("grow" * time)

    def plant_kingdom(self):
        print("the orchid belongs to the plant kingdom ")




orchid1 = orchid("Blue","summer","Falenopsis ")

orchid2 = orchid("red","spring","Dendrobium  ")
orchid3 = orchid("white","autumn","Cymbidium  ")

print(orchid1.__dict__)

orchid2.plant_kingdom()
