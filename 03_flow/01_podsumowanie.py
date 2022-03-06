# 1▹ Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście.

y = str(input("Wpisz liczbę imiona (możesz użyć przecinka lub znaku białego) :"))
x = []

x.append(y)



for a in range(len(x)):
    print("Hello", x[a], end=" ")