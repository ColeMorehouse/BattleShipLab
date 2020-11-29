import tkinter as tk
import tkinter.font as font
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
print("test")
print(player1.board1.toString())


class GUI:
    def __init__(self):
        root = tk.Tk()
        T = tk.Text(root, height=110, width=110)
        T.pack()
        T.insert(tk.END, player1.board1.toString())
        tk.mainloop()

GUI()
