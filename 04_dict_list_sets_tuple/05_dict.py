# 5. W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
#
# """Szybko, zbudź się, szybko, wstawaj
# Szybko, szybko, stygnie kawa
# Szybko, zęby myj i ręce"""
# Zadbaj o sposób wyświetlania np.:
#
# szybko : 5
#
# zbudź : 1

txt = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

print(txt)

txt = txt.replace(",","")


txt = txt.lower()
words = txt.split()
print(words)

count_dict = {}

for word in words:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1
print(count_dict)

for k,v in count_dict.items():
    print(k," ----->",v)

#słownik 8
#reszta po jednym zadaniu