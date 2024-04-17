def print_segment(n, max_width):
    for size in range(1, n+1, 2):
        print((size * "*").center(max_width))

def show_tree(base):
    for lvl in range(3, base+1, 2):
        print_segment(lvl, base)

while(True):
    n = int(input("Podaj maksymalną podstawę drzewa (nieparzystą) : "))
    if n % 2 == 0:
        print("Spróbuj jeszcze raz")
    else:
        break
show_tree(n)