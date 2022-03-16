# 6▹ Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.
import random




def game_result(player_wins,python_wins):
    print("_______________________________________________________________________")
    print("koniec rund")
    if player_wins > python_wins:
        print("Wygrałeś")

    elif player_wins == python_wins:
        print("Remis")

    else:
        print("Przegrałeś")

    return

def main_game_structure(rounds):
    python_wins = 0
    player_wins = 0
    i = 0
    while i != rounds:
        gamelist = ["k", "p", "n"]
        python_choice = random.choice(gamelist)
        player_choice = input("Podaj figuerę: ").lower()

        if player_choice == "koniec":
            print("Koniec gry")
            break
        elif player_choice == python_choice:
            i += 1
            print("Runda:", i)
            print("Remis")
        elif player_choice == "n":

            if python_choice == "k":
                i += 1
                print("Runda:", i)
                python_wins += 1
                print("Przegrałeś", "Python: ", python_wins, "Gracz: ", player_wins)

            else:
                i += 1
                print("Runda:", i)
                player_wins += 1
                print("Wygrałeś", "Python: ", python_wins, "Gracz: ", player_wins)
        elif player_choice == "p":

            if python_choice == "n":
                i += 1
                print("Runda:", i)
                python_wins += 1
                print("Przegrałeś", "Python: ", python_wins, "Gracz: ", player_wins)
            else:
                i += 1
                print("Runda:", i)
                player_wins += 1
                print("Wygrałeś", "Python: ", python_wins, "Gracz: ", player_wins)
        elif player_choice == "k":

            if python_choice == "p":
                i += 1
                print("Runda:", i)
                python_wins += 1
                print("Przegrałeś", "Python: ", python_wins, "Gracz: ", player_wins)
            else:
                i += 1
                print("Runda:", i)
                player_wins += 1
                print("Wygrałeś", "Python: ", python_wins, "Gracz: ", player_wins)
    y = python_wins
    x = player_wins
    game_result(x, y)

print("Gra kamien -(k) papier -(p) nożyce -(n)")
print("----------------------------------------")

rounds = int(input("Podaj liczbę rund: "))



main_game_structure(rounds)


