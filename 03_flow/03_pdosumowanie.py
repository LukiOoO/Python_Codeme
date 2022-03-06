# 3▹ W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.
#

lower = 0
upper = 0
specail = 0

x = input("Podaj ciąg znaków: ")

for i in x:
    if  i.isupper():
        upper += 1
print("Dużych liter w tekstcie jest: ", upper)


for i in x:
    if i.islower():
        lower += 1
print("Małych liter w teksice jest: ", lower)


for i in x:
    if i == "!" or i == "@" or i == "#" or i == "$" or i == "%" or i == "^" or i == "&" or i == "*" or i == "?":
        specail += 1
print("Znaków specjalnych w tekscie jest: ",specail)

