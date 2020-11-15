from Board import Board
from Player import Player
from ai import ai


#Create a board for player 1 and player
b1h = Board()
b1v = Board()

b2h = Board()
b2v = Board()

player1 = Player(b1h, b1v)
#Create a hidden board for player 1 and player 2
#Create player 1 and player 2


player2 = ai(b2h, b2v)
player2.getBoard().printBoard()