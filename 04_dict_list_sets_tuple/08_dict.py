# 8▹ Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich. Zapisz imiona w wersji anglojęzycznej. Dodaj wszystki listy razem. Nowa lista powinna zawierać 100 elementów.
#
# Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.


names_in_europe = {
        "Belgium": ["Emma","Mila","Louise","Elise","Lina","Alice","Camille","Sofia","Juliette","Lina"],
        "Spain" : ["Alba","Ana","Antonella","Ainhoa","Aitana","Andrea","Angela","Ana ","Carmen","Clara"],
        "Germany": ["Marie ","Sophie","Maria ","Emma ","Emilia ","Mia ","Anna ","Hannah","Johanna ","Sofia "],
        "Sweden": ["Emma","Elin","Ida","Hanna","Maja","Moa","Amanda","Alice","Linnea","Ella"],
        "Italy": ["Adele","Domenica","Camilla","Eva","Editta","Giulia","Domenica","Alice","Rosa","Valentina"],
        "Denmark": ["Isabella","Ida","Emma","Freja","Laura","Sofie","Maja","Caroline","Mathilde","Anna"],
        "France": ["Agathe ","Camille","Dominique ","Monique ","Nathalie ","Sophie ","Yvonne ","Laure ","Adrienne","Claire "],
        "Poland": ["Anna", "Justyna", "Ewa", "Barbara", "Kamila", "Zofia", "Julia", "Elwira", "Paulina", "Patrycja"],
        "England": ["Emma", "Olivia", "Louise", "Mila", "Elise", "Alice", "Lina", "Juliette", "Sofia", "Camille"],
        "Greece": ["Dorothea ","Eftychija ","Argiro ","Sofija ","Fotini ","Elpida ","Anti ","Lemonia ","Zoi","Irini "],
}

general_list = list(sorted(names_in_europe.values()))

print(general_list)

lists = []
for i in general_list:
    lists += i

print(lists)
repetitive_name = []
for x in lists:
    counter = lists.count(x)
    if counter >= 3:
        repetitive_name.append(x)
    else:
        continue

set_repetitive_name = set(repetitive_name)



print("Powtarzające się imiona to: ",*set_repetitive_name)