# 4▹ Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

lists = []

counter = 0

c = int(input("Podaj ilość elementów (Parzysta) : "))
while counter < c:
    x = input("Podaj przystą ilość liczb: ")
    lists.append(x)
    counter += 1

print(lists)




def the_same_middle_list_element():
    if lists[int(len(lists)/2)] == lists[int(len(lists)/2)-1]:
        print(lists[int(len(lists)/2)])
        print(lists[int(len(lists)/2)-1])
    else:
        print("Nie ma takich samych liczb w środku")

the_same_middle_list_element()