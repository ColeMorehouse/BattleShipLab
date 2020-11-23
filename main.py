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

#player1.setUpBoard()
player1.autoDraft()
print("player 1 board: ")
player1.getB1().printBoard()
print("player 1 guessboard: ")
player1.getGb().printGb()
player2 = ai(b2, b2g)
print("ai board: ")
player2.getBoard().printBoard()
print("ai Guess Board: ")
player2.getGBoard().printGb()


print("ai's turn: ")
player2.guessSpace(player1.getB1())
print("ai Guess Board: ")
player2.getGBoard().printGb()
print("player board after ai guess: ")
player1.getB1().printBoard()

print("player 1's turn: ")
player1.guessSpace(player2.getBoard())
print("player 1's Guess Board: ")
player1.getGb().printGb()
print("ai's board after p1 guess: ")
player2.getBoard().printBoard()
