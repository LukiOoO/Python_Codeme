# 1▹ Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek. Każda z nich powinna dziedziczyć z nadrzędnej klasy Ssaki.
# Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta.
# Utwórz obiekty klas - kot, pies i człowiek, udowodnij, że rzeczywiście korzystają z klas rodziców.

# 2▹ Do klasy człowiek dodaj metodę super() tak, aby móc wyświetlić opis dostępny gdziekolwiek w klasie ssaki.





class animals():
    def animal(self):
        print("Im animal")



class mammals(animals):
    def mammals(self):
        print("Im mammals")

    def mamals_description(self):
        print("A mammal is an animal that breathes air, has a backbone, and grows hair at some point during its lif")

class cat(mammals):
    def cat(self):
        print("MIAL")


class dog(mammals):
    def dog(self):
        print("HOW HOW")



class human(mammals):
    def __init__(self):
        super(human, self).mamals_description()
        print("Im human")


dog = dog().animal()
cat = cat().mammals()
human = human()

