# 2▹ Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).


def min_of(y,x):
    return x if x < y else y

def minimum_of(a,b,c):
    minimum = min_of(a,b)
    return min_of(minimum,c)



print("Najmniejsza wartość to: ", minimum_of(22,2,3))