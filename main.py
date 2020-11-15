from Board import Board
from Board import gBoard
from Player import Player
from ai import ai


#Create a board for player 1 and player
b1 = Board()
b2 = Board()

b1g = gBoard(b2)
b2g = gBoard(b1)

player1 = Player(b1, b1g)
#Create a hidden board for player 1 and player 2
#Create player 1 and player 2

player1.setUpBoard()
print("player 1 board: ")
player1.getB1().printBoard()
print("player 1 guessboard: ")
player1.getGB.printGB()
player2 = ai(b2, b2g)
player2.getBoard().printBoard()