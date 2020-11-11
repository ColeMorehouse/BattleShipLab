from Board import Board
from Ships import Ships
from Player import Player


#Create a board for player 1 and player
p1b = Board() #test changegit
p1gb = gBoard()

p2b = Board()
p2gb = gBoard()

player1 = Player(p1b, p1gb)
#Create a hidden board for player 1 and player 2
#Create player 1 and player 2
player2 = p2(p2b, p2gb)

player1.setUpBoard()
player2.setUpBoard()

notwin = true

while notwin:
  for x in range(10):
    row = input("Player 1! Enter row of guess: ")
    col = input("Player 1! Enter column of guess: ") 
    gRet = p2b.guess(row, col)
    if gRet == "out of bounds" or gRet == "already guessed":
      x -= 1
      print (gRet)
    else:
      p1gb.doGuess(p2b)
      
      p1b.printBoard()
      p1gb.printGB()
      p2b.printBoard()
      p2gb.printGB()
    
 # add shit here
