#  File:       Battleship_Game.py
#  Purpose:    Game :Simplified version of the classic board game Battleship!
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Monday 29th August 2016, 05:30 PM

from random import randint

board = []
for i in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for item in board:
        print ("  ".join(item))

print_board(board)

def random_row(board):
    return randint(0,len(board)-1)

def random_col(board):
    return randint(0,len(board)-1)

ship_row = random_row(board)
ship_col = random_col(board)

guess_row = int(input("Guess Row:"))
guess_col = int(input("Guess Col: "))

print (ship_col)
print (ship_row)

if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You destroyed my battleship!")

else:
     if guess_row == range(5) and guess_col == range(5):
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
        print_board(board)
    else:
        print "Oops, that's not even in the ocean."
