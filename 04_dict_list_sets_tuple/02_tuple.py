# 2▹ Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

tuplex = (1,1,1,2,3,"kot","pies","kot")

s = set(tuplex)

s.remove(2)
s.remove("pies")
s.remove(3)
c = tuple(s)
print(c)

