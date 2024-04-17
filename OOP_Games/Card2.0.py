import random


class Card:
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + ' '
        else:
            rep = '<empty>'

        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("I can't continue to distribute. I ran out of cards!")


if __name__ == '__main__':
    deck1 = Deck()
    print("A new deck has been created.")
    print("Deck:")
    print(deck1)

    deck1.populate()

    print("I added a set of cards to the deck.")
    print("Deck:")
    print(deck1)

    deck1.shuffle()

    print("I have shuffled a deck of cards.")
    print("Deck:")
    print(deck1)

    my_hand = Hand()
    your_hand = Hand()
    hands = [my_hand, your_hand]

    deck1.deal(hands, per_hand=5)

    print("I have dealt myself and you 5 cards each.")
    print("My hand:")
    print(my_hand)
    print("Your hand:")
    print(your_hand)
    print("Deck:")
    print(deck1)

    deck1.clear()
    print("I have cleared the contents of the deck.")

    print("deck:", deck1)
    input("To end the program, press the Enter key.")

