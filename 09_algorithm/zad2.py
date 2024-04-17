def sum_naturals_for(n):
    sum_numbers = 0

    for num in range(n + 1):
        sum_numbers += num

    return sum_numbers


# ------
def sum_naturals_while(n):
    sum_numbers = 0

    while n > 0:
        sum_numbers += n
        n = n - 1

    return sum_numbers


# ------

def sum_naturals_recursion(n):
    if n == 1:
        return 1
    else:
        return n + sum_naturals_recursion(n - 1)


def main():
    # result1 = sum_naturals_for(10)
    # print('---')
    # print('for', result1)

    # result2 = sum_naturals_while(10)
    # print('---')
    # print('while', result2)

    result3 = sum_naturals_recursion(10)
    print('recursion', result3)


if __name__ == '__main__':
    main()