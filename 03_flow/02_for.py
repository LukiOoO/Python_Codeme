# 2Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać. Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.

recipe = ["Mąka pszenna", "Mleko", "Woda gazowana", "cukier wanlinowy", "oliwa z oliwek"]
make_recipie = ["Zmiksuj składniki poza olejem", "Odstaw ciasto na 15 min", "smaż naleśniki na rozgrzanym oleju "
                ,"odwaracj i zdejmi"]


for i in recipe:
    print(i, end=", ")

print()

for x in range(1, len(make_recipie) + 1):
    print(x,make_recipie[x -1])



