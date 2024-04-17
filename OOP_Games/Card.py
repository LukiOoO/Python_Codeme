
class Card:
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


if __name__ == '__main__':
    card1 = Card(rank='A', suit='♣')
    print('I display the card object (Card class):')
    print(card1)
    card2 = Card(rank='2', suit='♣')
    card3 = Card(rank='3', suit='♣')
    card4 = Card(rank='4', suit='♣')
    card5 = Card(rank='5', suit='♣')
    print('\n I display the rest of the objects one at a time:')
    print(card2)
    print(card3)
    print(card4)
    print(card5)

