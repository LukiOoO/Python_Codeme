# 6▹ Poznaj trójkąt Pascala. Napisz kod, który wyświetla trójkąt Pascala dla podanego N.



def main(y):
    listx = []
    for i in range(y):
        temp_list = []
        for x in range(i+1):
            if x == 0 or x == i:
                temp_list.append(1)
            else:
                temp_list.append(listx[i-1][x-1]+listx[i-1][x])
        listx.append(temp_list)
    for i in range(y):
        for x in range(y-i-1):
            print(' ',end='')
        for x in range(i+1):
            print(format(listx[i][x]),end=' ')
        print()


if __name__ == '__main__':
    y = int(input("Podaj liczbę: "))
    main(y)
