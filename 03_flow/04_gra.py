#  Napisz grę - kamień (k) / papier (p) / nożyce (n).
#
# Użytkownik podaje jedną z 3 figur.
#
# Komputer losuje jedną z 3 figur.
#
# Sprawdź kto wygrał tę rundę.
#
# Zmień kod tak, by użytkownik mógł podac liczbę rund.
#
# Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
#
# Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’
import random




print("Gra kamien -(k) papier -(p) nożyce -(n)")
print("----------------------------------------")

gamelist = ["k","p","n"]



rounds = int(input("Podaj liczbę rund: "))

python_wins = 0
player_wins = 0
i = 0
while i != rounds:
    python_choice = random.choice(gamelist)
    player_choice = input("Podaj figuerę: ").lower()


    if player_choice == "koniec":
        print("Koniec gry")
        break
    elif player_choice == python_choice:
        i += 1
        print("Runda:",i)
        print("Remis")
    elif player_choice == "n":

        if python_choice == "k":
            i += 1
            print("Runda:",i)
            python_wins += 1
            print("Przegrałeś","Python: ", python_wins,"Gracz: ", player_wins)

        else:
            i += 1
            print("Runda:",i)
            player_wins += 1
            print("Wygrałeś","Python: ",python_wins,"Gracz: ",player_wins)
    elif player_choice == "p":

        if python_choice == "n":
            i += 1
            print("Runda:",i)
            python_wins += 1
            print("Przegrałeś","Python: ",python_wins,"Gracz: ",player_wins)
        else:
            i += 1
            print("Runda:",i)
            player_wins += 1
            print("Wygrałeś","Python: ",python_wins,"Gracz: ",player_wins)
    elif player_choice == "k":

        if python_choice == "p":
            i += 1
            print("Runda:",i)
            python_wins += 1
            print("Przegrałeś","Python: ",python_wins,"Gracz: ",player_wins)
        else:
            i += 1
            print("Runda:",i)
            player_wins += 1
            print("Wygrałeś","Python: ",python_wins,"Gracz: ",player_wins)


print("_______________________________________________________________________")
print("koniec rund")
if player_wins > python_wins:
    print("Wygrałeś")

elif player_wins == python_wins:
    print("Remis")

else:
    print("Przegrałeś")
