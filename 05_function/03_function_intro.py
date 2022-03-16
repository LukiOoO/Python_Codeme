# 3▹ Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.


def numbers_sum(numbers):
    return sum(numbers)


#--------- glowna czesc skryptu:

list_of_numbers = [1,2,2,333,45]
total = numbers_sum((list_of_numbers))
print(total)