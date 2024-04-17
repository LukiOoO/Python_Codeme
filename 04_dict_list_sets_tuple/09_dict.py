# 9▹ 5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach. Wyświetl najpopularniejszy przedmiot.
# (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery)
import statistics
from statistics import mode




lists1 = []

counter = 0



while counter < 4:
    c = input("User1 podaj 4 przedmioty szkolne: ")
    counter += 1
    if c.isupper() or c.islower() and not c.isupper() or not c.islower() :
        lists1.append(c)
    else:
        print("coś poszło nie tak")
counter = 0
while counter < 4:
    c = input("User2 podaj 4 przedmioty szkolne: ")
    counter += 1
    if c.isupper() or c.islower() and not c.isupper() or not c.islower() :
        lists1.append(c)
    else:
        print("coś poszło nie tak")

counter = 0

while counter < 4:
    c = input("User3 podaj 4 przedmioty szkolne: ")
    counter += 1
    if c.isupper() or c.islower() and not c.isupper() or not c.islower() :
        lists1.append(c)
    else:
        print("coś poszło nie tak")
counter = 0


while counter < 4:
    c = input("User4 podaj 4 przedmioty szkolne: ")
    counter += 1
    if c.isupper() or c.islower() and not c.isupper() or not c.islower() :
        lists1.append(c)
    else:
        print("Poszło nie tak")

counter = 0

while counter < 4:
    c = input("User 5 podaj 4 przedmioty szkolne: ")
    counter += 1
    if c.isupper() or c.islower() and not c.isupper() or not c.islower() :
        lists1.append(c)
    else:
        print("coś poszło nie tak")





print("Predmiot który się powtarza najwięcje razy to: ", mode(lists1))

