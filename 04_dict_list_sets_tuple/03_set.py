# 3▹ Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki, a oraz nieparzystych elementów z drugiej. Przekształć powstałą listę w set.

tuple1 = tuple(range(0,10))
print(tuple1)

tuple2 = ("a","b","c","d","e","f")

tmp_list = list(tuple1[::2] + tuple2[1::2])
print(tmp_list)
temp_set = set(tmp_list)

print(temp_set)