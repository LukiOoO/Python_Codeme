# 3▹ Wyświetl tylko 5 pierwszych linii

def read_txt():
    with open("tekst.txt","r",encoding="utf-8") as fopen:
        txt = [next(fopen).strip() for x in range(3)]

    return txt


def print_lines():
    for x in read_txt():
        print(x)


print_lines()

