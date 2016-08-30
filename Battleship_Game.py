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
print ("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0,len(board)-1)

def random_col(board):
    return randint(0,len(board)-1)

ship_row = random_row(board)
ship_col = random_col(board)
for turn in range(4):
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col: "))

    print (ship_col)
    print (ship_row)

    # Everything from here on should go in your for loop!

    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sank my battleship!")
    else:
        if guess_row == range(5) and guess_col == range(5):
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            print_board(board)
        elif board[guess_row][guess_col] == "X":

            print ("You guessed that one already.")
        else:
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            print ("Turn", turn + 1)
    if turn == 3:
        print ("Game Over")
    print_board(board)
