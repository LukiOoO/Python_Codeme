# 10▹ Stwórz grę wisielec “bez wisielca”.
#
# Komputer losuje wyraz z dostępnej w programie listy wyrazów.
#
# Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)
#
# Użykownik podaje literę.
#
# Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat:
# “Trafione!” oraz napis ze znanymi literami.
#
# W przeciwnym wpadku pokaż komunikat:
# “Nie trafione, spróbuj jeszcze raz!”.
#
# Możesz ograniczyć liczbę prób do np. 10.
import random

# def random_word():
#     x = random.choice(sport_list)
#     print(x)
#     return x
'''
wystąpił mały problem jak miałem  to w kilku funkcjach dlatego postanowiłem zrobić w jednej
 
'''

def main_game():
    random_word = random.choice(sport_list)

    user_guess = ""
    try_number = 10
    try_counter = 0
    while try_counter < try_number:
        guess = input("\nPodaj literę: ")
        if guess in random_word:
            print(f"litera {guess} jest w tym słowie")
        else:
            try_number -= 1
            print(f"Litery {guess} nie ma w słowie zostało {try_number} prób")
        user_guess += guess
        wrong_count = 0
        for i in random_word:
            if i in user_guess:
                print(f"{i}",end="")
            else:
                print("_",end="")
                wrong_count += 1
        if wrong_count == 0:
            print(f"Wygrałeś sekretne słowo to {random_word}")
            break
    else:
        print(f"Przegraleś sekretne słowo to {random_word}")








sport_list = ["koszykowka", "bilard", "siatkowka", "boks", "mma", "badminton", "kolarstwo", "szachy","tenis"]
main_game()

# import random
#
#
# # Komputer losuje wyraz z dostępnej w programie listy wyrazów.
# # Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)
# # Użykownik podaje literę.
# # Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat:
# # “Trafione!” oraz napis ze znanymi literami.
# # W przeciwnym wpadku pokaż komunikat:
# # “Nie trafione, spróbuj jeszcze raz!”.
# # Możesz ograniczyć liczbę prób do np. 10.
#
#
# def check_win(l_visible, l_hidden, random_p, counter):
#     if l_visible == l_hidden:
#         print("Brawo, wygrałeś!")
#         return True
#     elif counter == 10:
#         print(f"Niestety, przegrałeś - twoim hasłem było: {random_p}")
#
#
# def game_rules(random_p):
#     rundy = 10
#     counter = 0
#     l_hidden = []
#     l_visible = []
#     for i in random_p:
#         l_hidden.append("-")
#         l_visible.append(i.lower())
#
#     print(l_visible)
#     while counter < rundy:
#         counter += 1
#         print(*l_hidden)
#         user_input = input("\n Podaj literkę: \n")
#
#         if user_input in l_visible:
#             for i in range(len(l_visible)):
#                 if l_visible[i] == user_input:
#                     l_hidden[i] = user_input
#         else:
#             print(f"Literki: {user_input} nie ma w tym wyrazie.")
#             print(f"Pozostała liczba prób: {rundy - counter}")
#
#         print(counter)
#
#         if check_win(l_visible, l_hidden, random_p, counter):
#             break
#
#
# def main():
#     random_words = ["Skrzydło", "Ananas", "Kosmiczny", "Kalendarz", "Kamień",
#                     "Kierowca", "Syrenka", "Wulkan", "Biegunka", "Tęcza",
#                     "Kapelusz", "Cytryna", "Korona", "Kaktus", "Lornetka",
#                     "Jaszczurka", "Dzwonek", "Słowik", "Nocnik", "Krater",
#                     "Lampion", "Banan", "Murmeltier", "Rowerzysta", "Cyfrowy",
#                     "Orzech", "Rondo", "Wir", "Zebra", "Migdał",
#                     "Szalik", "Furgonetka", "Strzała", "Kwarc", "Pilot",
#                     "Sardynka", "Bazylia", "Karuzela", "Juka", "Szkatułka",
#                     "Szarlotka", "Dźwig", "Tornister", "Czapka", "Manekin",
#                     "Karton", "Kompas", "Filizanka", "Chmura", "Pudło"]
#
#     random_p = random.choice(random_words)
#     game_rules("anna")
#
#
# if __name__ == '__main__':
#     main()