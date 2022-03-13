# Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi). Następnie rozpakuj tę krotkę na pojedyńcze zmienne.
# Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie np. “Mój pies, rasy border collie wabi się Dyzio”.


animal = ("jaszczurka", "agama brodata", "edward")

(animal , race, name) = animal

print(f"Moim zwierzęciem jest {animal} jest to {race} nazywa się {name} ")