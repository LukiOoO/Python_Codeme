from random import  randint


class Player:
    def blast(self, enemy):
        print('The player is hitting the enemy with a laser. \n')
        enemy.die()

    def lost(self):
        print('Alien eats player and inhides planet')



class Alien:
    def die(self):
        print(" The stranger struggles to catch his breath, It's over. But truly in" ,
               "We fought until the end. No, it's not the end. My larvae unite "
                "Oh yes they will avenge me one day.... \n,"
                "Farewell, cruel Universe! Im dieeeeeeeeeeee")

    def win(self, enemy):
       enemy.lost()



if __name__ == '__main__':
    print('************ Death of an Alien ************')
    hero = Player()
    ivader = Alien()

    if randint(0, 10) >= 3:
        hero.blast(ivader)
        input('\n\n  To end the program, press the Enter key.')

    else:
        ivader.win(hero)
