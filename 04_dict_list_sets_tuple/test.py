list = [1,4,5,222,141,123,414,55,5,9,1,1,1]
print(list)

list2 = list.copy()
print(list2)

list2.sort()
print(list2)

list2_sorted = sorted(list2)
print(list2_sorted)

list2.clear()
print("Wyczyszczona ",list2)

count = list.count(1)
print(count)

print(sum(list))
