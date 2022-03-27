# 6▹ Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych. Sprawdź dla każdej kart jej typ.
# Podziel kart do plików wg typów np. visa.txt, mastercard.txt, americanexpress.txt.




def open_file():
    with open("karty.txt","r" ,encoding="utf-8") as f:
        c = f.readlines()
    return c


def is_american_express(card_number):
    card_length = len(card_number)
    return card_length == 15 and (card_number[0:2] == '34' or card_number[0:2] == '37')


def is_visa(card_number):
    card_length = len(card_number)
    return card_length in [13, 16] and card_number[0] == '4'


def is_mastercard(card_number):
    card_length = len(card_number)
    starts_with_51_55 = 51 <= int(card_number[0:2]) <= 55
    starts_with_2221_2720 = 2221 <= int(card_number[0:4]) <= 2720

    return card_length == 16 and (starts_with_51_55 or starts_with_2221_2720)

def write_to_file(filename):
    with open(filename ,"w",encoding="utf-8") as f:
        x = str(open_file())
        f.write(x)




new_list = []


for x in open_file():
    new_list.append(x.rstrip("\n").replace(" ",""))

print(new_list)

for x in range(len(new_list)):
    if is_american_express(new_list[x]):
        write_to_file(new_list[x])
    if is_mastercard(new_list[x]):
        write_to_file("mastercard.txt")
    if is_visa(new_list[x]):
        write_to_file("visa.txt")
