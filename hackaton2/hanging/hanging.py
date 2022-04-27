import random
import collections
from print import print_hang_man
from print_turtle import turtle_print
def radom_word():
    with open("word",encoding="utf-8") as f:
        x = f.readlines()
    return random.choice(x).rstrip("\n")


def main_game(random_word):
    user_guess = ""
    try_number = 10
    list1 = [",", ".", "/", "?", ";", "'", "[", "]", "-", " "]
    try_counter = 0
    print(random_word)
    while True:
        try:
            while try_counter < try_number:
                guess = input("\nEnter a letter: ")
                if guess.isdigit() or guess in list1:
                    raise ValueError
                if guess in random_word:
                    print(f"The letter {guess} is in this word ")
                else:
                    try_number -= 1
                    print_hang_man(try_number)
                    turtle_print(try_number)
                    print(f"The letter {guess} not in the word there are {try_number} attempts left")
                user_guess += guess
                wrong_count = 0
                for i in random_word:
                    if i in user_guess:
                        print(f"{i}",end="")
                    else:
                        print("_",end="")
                        wrong_count += 1
                if wrong_count == 0:
                    print(f"You won the secret word is {random_word}")
                    break
            else:
                print(f"You lost the secret word it {random_word}")
            break
        except ValueError:
            print("Letters only")


if __name__ == '__main__':
    random_word = radom_word()
    main_game(random_word)
