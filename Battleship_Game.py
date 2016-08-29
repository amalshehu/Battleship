#  File:       Battleship_Game.py
#  Purpose:    Game :Simplified version of the classic board game Battleship!
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Monday 29th August 2016, 05:30 PM


board = []
for i in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for item in board:
        print ("  ".join(item))

print_board(board)
