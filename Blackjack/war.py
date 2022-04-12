# ▷ 2. Napisz obiektową, jednokartową wersję gry w wojnę, w której każdy otrzymuje jedną kartę i gracz z najwyższą kartą wygrywa.
import random

#do dokończenia
class Card:
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit


class player_s():
    def ask_number(question, low, high):
        """Poproś o podanie liczby z określonego zakresu."""
        response = None
        while response not in range(low, high):
            response = int(input(question))
        return response

    def ask_yes_no(question):
        """Zadaj pytanie, na które można odpowiedzieć tak lub nie."""
        response = None
        while response not in ("t", "n"):
            response = input(question).lower()
        return response



class Hand:
      """ Ręka - karty do gry w ręku gracza. """
      def __init__(self):
          self.cards = []

      def __str__(self):
          if self.cards:
              rep = ""
              for card in self.cards:
                  rep += str(card) + " "
          else:
              rep = "<pusta>"
          return rep

      def clear(self):
          self.cards = []

      def add(self, card):
          self.cards.append(card)

      def give(self, card, other_hand):
          self.cards.remove(card)
          other_hand.add(card)


def main():
    print("Witaj w grze 'Wojna'!\n")
    players = []
    players_num = player_s.ask_number("Podaj liczbe graczy od 2 - 7: ", low=2 ,high=8 )
    for i in range(players_num):
        name = input("Wprowadź nazwy graczy: ")
        players.append(name)
    again = None
    while again != "n":
        player = Hand()


        player_s.ask_yes_no("\n Czy chcesz zagrać pownownie: ")




if __name__ == "__main__":
    main()