import time
import colorama
import sys
import Base_Card_Module as BcM
import SimpleGameModule as SgM


class BJCard(BcM.Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJCard.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v


class BJDeck(BcM.Deck):
    def populate(self):
        for suit in BJCard.SUITS:
            for rank in BJCard.RANKS:
                self.cards.append(BJCard(rank, suit))


class BJHand(BcM.Hand):
    def __init__(self, name):
        super(BJHand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ':\t' + super(BJHand, self).__str__()
        if self.total:
            rep += '(' + str(self.total) + ')'
            return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        for card in self.cards:
            t += card.value
        contains_ace = False
        for card in self.cards:
            if card.value == BJCard.ACE_VALUE:
                contains_ace = True
        if contains_ace and t <= 11:
            t += 10
        return t

    def is_busted(self):
        return self.total > 21


class BJPlayer(BJHand):
    def __init__(self, name, assets, play):
        super().__init__(name)
        self.assets = float(assets)
        self.stake = self.set_stake()
        self.play = str(play)

    def set_stake(self):
        cash = float(input(f'{self.name} Your assets {self.assets}. How much money do you bet?: '))
        while cash < 100 or cash > self.assets:
            if cash > self.assets:
                print("You can't bet more than you have")
            else:
                print('Minimum bet 100$')
            cash = float(input(f'{self.name} Your assets {self.assets}. How much money do you bet?: '))
        return cash

    def update_assets(self):
        return self.assets - self.stake

    def profit_or_loss(self):
        if self.assets > 1000:
            print(f'{self.name} you have {self.assets} your profit is {colorama.Fore.GREEN}'
                  f'{self.assets - 1000}{colorama.Style.RESET_ALL}')

        elif self.assets < 1000:
            print(f'{self.name} you have {self.assets} you have lost {colorama.Fore.RED} '
                  f'{1000 - self.assets}{colorama.Style.RESET_ALL}')

        else:
            print(f"{self.name} {colorama.Fore.YELLOW}  you haven't won or lost anything "
                  f"{colorama.Style.RESET_ALL}")

    def update_stake(self):
        self.stake = self.set_stake()

    def is_hitting(self):
        response = SgM.ask_yes_no('\n' + self.name + ' Do you want to pick a card, (y - Yes) or (n - No) ')
        return response == 'y'

    def bust(self):
        print(f'{self.name},{colorama.Fore.RED} have a bust. {colorama.Style.RESET_ALL}')
        return self.assets - self.stake

    def lose(self):
        print(f'{self.name},{colorama.Fore.RED} losing. {colorama.Style.RESET_ALL}')
        return self.assets - self.stake

    def win(self):
        print(f'{self.name},{colorama.Fore.GREEN} win . {colorama.Style.RESET_ALL}')
        win_cash = self.stake * 1.5
        assets_now = self.update_assets()
        return assets_now + win_cash

    def push(self):
        print(f'{self.name},{colorama.Fore.YELLOW} tie. {colorama.Style.RESET_ALL}')

    def end(self):
        print(f"{self.name},{colorama.Fore.RED} You lost all your money you can't play   {colorama.Style.RESET_ALL}")


class BJDealer(BJHand):
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(f'{self.name},{colorama.Fore.CYAN} have a bust. {colorama.Style.RESET_ALL}')

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJGame(object):
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJPlayer(name, 1000, 'yes')
            self.players.append(player)

        self.dealer = BJDealer('Dealer')
        self.deck = BJDeck()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                time.sleep(1)
                player.assets = player.bust()

    def remove_player(self, player_list):
        for player in player_list:
            self.players.remove(player)

    def check_can_play(self):
        players_to_del = []
        for player in self.players:
            if player.assets < 100 or player.assets == 0:
                print(f"{player.name}{colorama.Fore.RED} "
                      f"don't have enough money you can't keep playing"
                      f".{colorama.Style.RESET_ALL}")
                players_to_del.append(player)
        self.remove_player(players_to_del)
        if len(self.players) == 0:
            sys.exit()

    def again(self):
        for player in self.players:
            again = SgM.ask_yes_no(f"\n Would you like to play again {player.name} ?? (y - Yes) or (n - No): ")
            if again == 'n':
                player.play = 'not'

    def if_not_playing(self):
        players_to_del = []
        for player in self.players:
            if player.play == 'not':
                player.profit_or_loss()
                players_to_del.append(player)
        self.remove_player(players_to_del)

    def end(self):
        if len(self.players) == 0:
            print(f'{colorama.Fore.YELLOW} No one is playing anymore end {colorama.Style.RESET_ALL}')
            return False
        else:
            return True

    def play(self, i):
        self.deck.populate()
        self.deck.shuffle()
        self.deck.deal(self.players, per_hand=2)
        self.deck.deal([self.dealer], per_hand=2)

        self.dealer.flip_first_card()

        for player in self.players:
            if i >= 1:
                player.update_stake()
            print(f'{player} \t assets = {player.update_assets()}$ \t  stake = {player.stake}$')
        print(self.dealer.name, *self.dealer.cards)

        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()

        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            time.sleep(1)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                for player in self.still_playing:
                    time.sleep(1)
                    player.assets = player.win()
            else:
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        time.sleep(1)
                        player.assets = player.win()
                    elif player.total < self.dealer.total:
                        time.sleep(1)
                        player.assets = player.lose()
                    else:
                        time.sleep(1)
                        player.push()
        for player in self.players:
            player.clear()

        self.dealer.clear()
        self.deck.clear()
        self.check_can_play()
        self.again()
        self.if_not_playing()
        return self.end()


def main():
    print("Welcome to the game of 'Blackjack'! \n")
    names = []
    while True:
        try:
            number = SgM.ask_number('Enter the number of players (1 - 7):', low=1, high=8)

            for i in range(number):

                while True:
                    name = input("Enter the name of the player: ")
                    if name != '':
                        names.append(name)
                        break
                    else:
                        print('The field must not be empty ')
            print()
            game = BJGame(names)
            i = 0
            while game.play(i):
                i += 1
            break
        except ValueError:
            print("The value should be a number ")
            names.clear()


if __name__ == '__main__':
    main()
    input("To end the program, press the Enter key.")
