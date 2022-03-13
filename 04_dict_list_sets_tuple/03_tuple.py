# 3▹ Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby. Jeśli liczba znajduje się na krotce wyswietl jej indeks.

num = (1,2,3,4,5,6,7,8,9,-1,-2,-3)


i = int(input("Podaj liczbe: "))



if i in num:
    print(f"Indexem {i} jest: ", num.index(i,0,))
else:
    print("nie ma tej liczby")

