class Card:
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class UnprintableCard(Card):
    def __str__(self):
        return "<secreted>"


class PositionableCard(Card):
    def __init__(self, rank, suit, face_up=True):
        super().__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super().__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


if __name__ == '__main__':
    card1 = Card("A", "♥")
    card2 = UnprintableCard("A", "♥")
    card3 = PositionableCard("A", "♥")

    print("Displaying an object of class Card:")
    print(card1)

    print("\nDisplay object of class Unprintable_Card:")
    print(card2)

    print("\nDisplay object of class Positionable_Card:")
    print(card3)

    print("Reversing the state of an object of class Positionable_Card (discover-cover)")
    card3.flip()

    print("Displaying an object of class Positionable_Card:")
    print(card3)
    input("To exit the program, press the Enter key.")

