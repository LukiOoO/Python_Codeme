import SimpleGameModule as SgM, random

if __name__ == "__main__":
    print("Welcome to the easiest game in the world!")
    again = None

    while again != "n":
        players = []
        num = SgM.ask_number(question="Enter the number of players (2 - 5): ", low=2, high=5)

        for i in range(num):
            name = input("Player name: ")
            score = random.randrange(100) + 1
            player = SgM.Player(name, score)
            players.append(player)
        print("\nThe results of the game:")
        for player in players:
            print(player)

        again = SgM.ask_yes_no("Do you want to play again? (t/n): ")
        input("To end the program, press the enter key.")