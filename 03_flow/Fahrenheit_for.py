# 1) Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach. Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
#
# C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
#
# Napisz rozwiązanie zarówno z użyciem pętli while jak i for.



f_degree = 0


c_degree = 5/9 * (f_degree - 32)

for i in range(1,12):
    c_degree = 5 / 9 * (f_degree - 32)
    print(f"{f_degree}, f =  {c_degree} C")
    f_degree = f_degree + 20