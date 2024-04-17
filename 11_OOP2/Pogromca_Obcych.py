import random
class Player():
    """ Gracz w grze strzelance """

    def blast(self, enemy):
        print("Gracz razi wroga laserami.\n")
        enemy.die()

class Alien():
    """ Obcy w grze strzekabce"""
    def die(self):
        print('Obcy z trudem łapie oddech, "To już koniec. Ale prawdziwie wielki koniec... \n',
              'Walczyliśmy do końca. Nie, to nie koniec. Larwy moje jednoczcie się! \n',
              'O tak one pomszczą mnie pewnego dnia... \n',
              'Żegnaj, okrutny Wszechświecie! Umieeeraaam"')
    def eat_human(self, human):
        print("Alien mlaska i niszczy planete")

if __name__ == '__main__':
    print('************ Śmierć Obcego ************\n')
    hero = Player()
    invader = Alien()
    x = random.randint(0, 10)
    print("celność strzału to --->", x)
    if x >= 3:
        hero.blast(invader)
    else:
        invader.eat_human(hero)

    input('\n\nAby zakończyć program, naciśnij klawisz Enter.')