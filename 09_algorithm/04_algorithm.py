# 4▹ Napisz funkcję przeszukiwania połówkowego (binarenego), która przyjmuje dwa parametry - szukany element oraz listę elementów. Zwraca informację czy element jest obecny na liście, albo nie.
#
# Wejście:
#
# elem = 21
# Wyjście:
#
# Przyznam się że algorytmy nie są moją mocną stroną i przy niektórych pracahc inspirowałem się rozwiązaniami z interneru :(

pos = -1


def binary_schare(list, x):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u) // 2

        if list[mid] == x:
            globals()["pos"] = mid
            return True
        else:
            if list[mid] < x:
                l = mid + 1
            else:
                u = mid + 1
    return False

data = [3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12]
data.sort()
print(data)
li = [2, 3, 3, 6, 7, 12, 12, 15, 21, 34, 44, 45, 56]

if binary_schare(li, 21):
    print("jest na lisce", pos + 1)
else:
    print("nie ma")