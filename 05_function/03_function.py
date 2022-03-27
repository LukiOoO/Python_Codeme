# 3▹ Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).
#bez funcki min max

# def maximum_of(a,b,c):
#     if a > b and a > c:
#         print("najwieksza liczbą jest: ", a)
#     elif b > a and b > c:
#         print("najwieksza liczbą jest: ", b)
#     else:
#         print("najwieksza liczba jest: ", c)
#
# maximum_of(1,2,11)
#




# def max_of(x, y):
#     if x > y:
#         return x
#     else:
#         return y
#
# def maximum_of(a,b,c):
#     result = max_of(a, b)
#     max_value = max_of(result, c)
#     return max_value
#
#
# # --- main
# print("Największa wartość to",  maximum_of(4, 91, 28) )




def max_of(x, y):
    return x if x > y else y

def maximum_of(a,b,c):
    result = max_of(a, b)
    return max_of(result, c)


# --- main
print("Największa wartość to",  maximum_of(4, 119, 128))



# to samo ale z pętlą for


def maximum_of(a,b,c):
    pool = [a,b,c]
    maximum = pool[0]
    for value in pool:
        if value > maximum:
            maximum = value
    return maximum

print(maximum_of(23,332,4))
