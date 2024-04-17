from Card import Card


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


if __name__ == '__main__':
    my_hand = Hand()
    print('I display the contents of my hand before adding any cards:')
    print(my_hand)

    card1 = Card(rank='A', suit='♣')
    card2 = Card(rank='2', suit='♣')
    card3 = Card(rank='3', suit='♣')
    card4 = Card(rank='4', suit='♣')
    card5 = Card(rank='5', suit='♣')

    my_hand.add(card1)
    my_hand.add(card2)
    my_hand.add(card3)
    my_hand.add(card4)
    my_hand.add(card5)

    print('I display the contents of my hand after adding 5 cards:')
    print(my_hand)

    your_hand = Hand()
    my_hand.give(card1, your_hand)
    my_hand.give(card2, your_hand)

    print("I am transferring the first two cards from my hand to yours.")
    print("----------------------------------")
    print("Your hand:")
    print(your_hand)
    print("My hand:")
    print(my_hand)

    my_hand.clear()
    print("My hand after removing cards from it:")
    print(my_hand)
    input("To exit the program, press the Enter key.")
    