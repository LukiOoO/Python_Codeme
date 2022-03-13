# 2▹ Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

number = []

#user_number = input("Podaj 10: ")

# number.append(user_number)
# print(number)

i = 1

while i <= 10:
    user_number = input("Podaj 10 liczb: ")
    i += 1
    number.append(int(user_number[0:]))




for i in number:
    if i % 2 == 0:
        print()
    else:
        print("Nieparzyte liczby które podałeś to:",i)
