# 4▹ Pomyśl co sprawia, że ssak jest ssakiem? Utwórz klasę ssaki.
# Stwórz kilka obiektów klasy ssaki np. wilk, koń, ssaki.


class ssaki():
    def __init__(self,obecnosc_owlosienia, stalocieplne, zyworodnosc):
        self.obecnosc_owlosienia = obecnosc_owlosienia
        self.stalocieplne = stalocieplne
        self.zyworodnosc = zyworodnosc


kon = ssaki("wlosie","38,5","tak")
delfin = ssaki("brak","37","tak")
pies = ssaki("sierść","38","tak")