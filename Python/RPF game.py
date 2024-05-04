#RPF game
#rock > scisscors, scissors > paper, paper > rock

import random

def play():
    user = input("Make a choice: \n'r' for rock, 'p' for paper, 's' for scissors:\n" )
    computer = random.choice(['r', 'p', 'f'])

    if user == computer:
        return 'It\'s a tie '
    
    if is_win(user, computer):
        return 'You won!'
    return 'you lost!'

def is_win(player, opponent):
    #return true if player wins
    if (player == 'r' and opponent == 's') or (player =='s' and opponent =='p')  or (player == 'p' and opponent == 'r'):
        return True
    

print(play())