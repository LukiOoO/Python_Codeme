#Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny. Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.
#
#Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.




cost = float(input("podaj cene paliwa: "))
usage = float(input("podaj spalanie na 100: ")) / 100
distance = int(input("Podaj dystans: "))

result = round(cost * usage * distance, 2)
print(f"Koszt wyprawy będzie wynosił  {result} zł")



