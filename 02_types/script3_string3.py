#3 Do zmiennej quote przypisz zdanie:
#„ Honesty is the first chapter in the book of wisdom.”, a następnie:
# Policz wszystkie znaki w napisie
# Nie modyfikując zmiennej wyświetl słowo wisdom
# Wyświetl tylko pierwszą połowę tekstu
# Wyświetl tylko kropkę
# Wyświetl od połowy tylko co trzecią literę cytatu
# Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
# Wyświetl cały cytat odwrotnie
# Zamień wisdom na słowo friendship



quote = "Honesty is the first chapter in the book of wisdom."

print(len(quote))
print(quote[-7:-1])


print(len(quote) // 2)
print(quote[0 : 25])

quoet2 = quote.strip("Honesty is the first chapter in the book of wisdom")
print(quoet2)


print(quote[25::3])

print()

quote4 = "Hnsyi h is hpe ntebo fwso."
print(quote4)
print(quote4[::-1])

print()

quote9 = quote.replace("wisdom", "friendship")
print(quote9)