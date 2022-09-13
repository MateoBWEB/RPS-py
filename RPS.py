#MB
#103
#RPS

import random

ROCK = 1
PAPER = 2
SCISSORS = 3

def wordChoice(num):
    if num == ROCK:
         return 'rock'
    elif num == PAPER: 
         return 'paper'
    elif num == SCISSORS:
         return 'scissors'
        
def rps(cmpc, player):
    if cmpc == player:
        print('Draw!')
        print()
        print('Let\'s play again...')
        main()
    if cmpc == ROCK:
        if player == PAPER:
            print('Player wins')
        elif player == SCISSORS:
            print('Computer wins')
    elif cmpc == PAPER:
        if player == ROCK:
            print('Player wraps rock')
            print('Computer Wins')
        elif player == PAPER:
            print('Player wins')
    elif cmpc == SCISSORS:
        if player == PAPER:
            print('Computer Wins')
        elif player == ROCK:
            print('Rock smashes scissors')
            print('Player wins')
        else:
            print('Invalid entry')
            
def main():
    cmpc = random.randint(1,3)
    #ask user for input
    player = int(input(\
        'Press\n1 for Rock\n2 for Paper\n3 for Scissors\n:'))
    print('Computer chooses ...',wordChoice(cmpc))

    rps(cmpc,player)
    
main()    
