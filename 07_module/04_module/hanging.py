# 4▹ Zmodyfikuj swoją grę wisielec tak, aby w dowolny uzasadniony sposób wykorzystać moduł lub moduły.




import random

# def random_word():
#     x = random.choice(sport_list)
#     print(x)
#     return x
'''
wystąpił mały problem jak miałem  to w kilku funkcjach dlatego postanowiłem zrobić w jednej

'''


def main():
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
                print(f"{i}", end="")
            else:
                print("_", end="")
                wrong_count += 1
        if wrong_count == 0:
            print(f"Wygrałeś sekretne słowo to {random_word}")
            break
    else:
        print(f"Przegraleś sekretne słowo to {random_word}")


sport_list = ["koszykowka", "bilard", "siatkowka", "boks", "mma", "badminton", "kolarstwo", "szachy", "tenis"]


if __name__ == "__main__":
    main()