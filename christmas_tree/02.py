# Kalendarz
# Opis:
#
# Poniżej mamy listą zawierającą krotki:

data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]
# Wyświetl kalendarz dla każdego miesiąca:
#
# January
#
# 00 01 02 03 04 05 06
# 07 08 09 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30
#

def make_view(month,day_range):
    print(month,'\n')

    for day in day_range:
        if day < 10:
            print('0' + str(day), end='\t')
        else:
            print(str(day), end='\t')

        if (day + 1) % 7 == 0:
            print()
    print()


data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]

for t in data:
    # print(t)
    make_view(t[0],t[1])
    print('---------------')