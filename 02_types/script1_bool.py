#1.Czy 23 + 3 będzie się równać 15 + 12 ?
result = (23 + 3) == (15 + 12)
print(result)
#2.Czy dzielenie 29 przez 7 bez reszty wynosi 5?
result2 = 29 // 7 == 5
print(result2)
#3.Czy 27 podzielone przez 8 daje resztę 3?
result3 = 27 % 8 == 3
print(result3)
#4.Wyświetl True, jeżeli liczba jest parzysta.
# niżej

#5.Czy 43 - 13 będzie się równać 11 + 12 ?
result5 = (43 - 13) == (11 + 12)
print(result5)
#6.Czy dzielenie 129 przez 17 bez reszty wynosi 3?
result6 = 129 // 17 == 3
print(result6)
#7.Czy 247 podzielone przez 5 daje resztę 2?
result7 = 247 % 5 == 2
print(result7)







# 4 inaczej
x = int(input("podaj liczbe: "))
if x % 2 == 0:
    print("True")
else:
    print("False")

# 4
num = int(input("Podaj liczbe od 1 - 100: "))
result4 = num % 2 == 0
print(result4)