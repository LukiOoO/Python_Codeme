# 5▹ Dysponując listą nazwisk uczestników uporządkuj ją leksykograficznie (alfabetycznie).
#
# Wejście:
#
# W pierwszym wierszu standardowego wejścia zapisano liczbę nazwisk N(1<= N <= 200). W następnych N wierszach zapisano po jednym nazwisku. Nazwisko rozpoczyna wielką litera, jego długość nie przekracza 50 znaków, i składa się tylko z liter alfabetu angielskiego.
#
# np.
#
# 4
# Lipski
# Kowal
# Adamiak
# Wojtczak
# Wyjście :
#
# W kolejnych wierszach wypisz nazwiska uczestników uporządkowane alfabetycznie.
#
# Adamiak
# Kowal
# Lipski
# Wojtczak


def name_sorted(name_list):
    name_list.sort()

    for i in name_list:
        print(i)

name_list = [ "Lipski", "Kowal" ,"Adamiak", "Wojtczak"]


if __name__ == "__main__":
    name_sorted(name_list)