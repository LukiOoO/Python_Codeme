# 5▹ Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:
#
# Dorota, Wellman, dziennikarka
#
# Adam, Małysz, sportowiec
#
# Robert, Lewandowski, piłkarz
#
# Krystyna, Janda, aktorka
#
# Wyświetl w sposób przyjazny dla użytkownika

people = [
    ["Dorota" ," Wellman" , " dziennikarka"],
    ["Adam", " Małysz", " sportowiec"],
    ["Robert", " Lewandowski", " piłkarz"],
    ["Krystyna"," Janda,"," aktorka"]


]




for i in people:
  print("---------_____-------")
  for ele in i:
      print(ele,end=" * ")
  print("----------------")