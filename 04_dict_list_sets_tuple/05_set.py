# 5▹ Porównaj zachowanie discard() vs remove() dla typu set.


set1 = {1,2,3,"kot","papuga"}


set1.discard("banan")
x = set1.discard("adam")
# metoda discard nie zwraca błędu jak elementu nie ma na liscie, zwraca liste lub none
print(set1)
print(x)
# metoda remove zwraca błąd gdy usuwanego elementu nie ma na lisce
set1.remove("ktos")

print(set1)