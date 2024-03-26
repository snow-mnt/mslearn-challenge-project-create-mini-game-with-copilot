# build the logic of the game
# there are three elements in the game: rock, paper, scissors
# the rock beats the scissors
# the scissors beat the paper
# the paper beats the rock

import random

def game(player):
    # generate a random number between 0 and 2
    computer = random.randint(0, 2)
    # convert the random number to the string of rock, paper, or scissors
    if computer == 0:
        computer = 'rock'
    elif computer == 1:
        computer = 'paper'
    else:
        computer = 'scissors'
    # check the result of the game
    if player == computer:
        return 'It is a tie!'
    elif player == 'rock':
        if computer == 'scissors':
            return 'You win!'
        else:
            return 'You lose!'
    elif player == 'paper':
        if computer == 'rock':
            return 'You win!'
        else:
            return 'You lose!'
    else:
        if computer == 'paper':
            return 'You win!'
        else:
            return 'You lose!'
        
# test the game
print(game('rock'))
print(game('paper'))
print(game('scissors'))
print(game('rock'))


