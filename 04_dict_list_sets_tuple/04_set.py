# 4▹ Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.
#
# input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
#
# output:
#
# [4, 3, 2, 1]
# [14, 13, 12, 11]
# [24, 23, 22, 21]

import numpy as np
lists = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

print(*np.array_split(lists, 3))

new_list1 = [1, 2, 3, 4]
new_list2 = [11, 12, 13, 14]
new_list3 = [21, 22, 23, 24]



new_list1.reverse()
print(new_list1)
new_list2.reverse()
print(new_list2)
new_list3.reverse()
print(new_list3)