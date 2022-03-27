# 4▹ Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)

even_list = []
def even_number(number):

    if number % 2 == 0:
        even_list.append(number)



c = int(input("Podaj ile licz wprowadzisz: "))
x = 0
while x < c :
    user_number = int(input("Podaj liczbę: "))
    even_number(user_number)
    x += 1

def print_number():
    if len(even_list) > 0:
        print("Parzyte lelementy to ",*even_list)
    else:
        print()

print_number()



