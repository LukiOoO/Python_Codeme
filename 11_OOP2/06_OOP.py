 # 6▹ Utworz klasę Kraj, która zawiera informację o powierzchni. ludności, jaki język jest urzędowy, jakie miasto jest stolicą.
# Utwórz klika obiektów klasy Kraj, stwórz listę obiektów klasy kraj, wyświetl elementy na liście krajów.

class country():
    def __init__(self, area, language, population, capital):
        self.area = area
        self.language = language
        self.population = population
        self.capital = capital




Polend = country("312 679 km²", "Polski", "37,95 miliona", "Warszawa")
England = country("130 279 km²", "Angielski", "55,98 miliona ", "Londyn")

country_list = [Polend.__dict__, England.__dict__]
print(country_list)



