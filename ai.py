from Board import Board
from Ships import ships
import random

class ai:

    def __init__(self, b1, b2):
        self.board1 = b1
        self.board2 = b2
        D = ships('D', LoR())
        S = ships('S', LoR())
        C = ships('C', LoR())
        B = ships('B', LoR())
        A = ships('A', LoR())


        self.keepPlacing(D, self.board1)

        self.keepPlacing(S, self.board1)
        
        self.keepPlacing(C, self.board1)
        self.keepPlacing(B, self.board1)
        self.keepPlacing(A, self.board1)


    def keepPlacing(self, ship, board):
        while (True):
            if board.placeShip(ship, random.randint(0, 9), random.randint(0, 9)) == "invalid location":
                continue
            else:
                break

    def getBoard(self):
        return self.board1

    def getGBoard(self):
        return self.board2

    #Guesses a space
    def guessSpace(self, b):
        #while everything is okey-dokey
        while True:
            x = random.randint(0,9)
            y = random.randint(0,9)
            gRet = b.guess(x, y)
            #if the guess is invalid
            if gRet != "already guessed" and gRet != "out of bounds":
                self.board2.doGuess(x, y, b)
                return

#Returns either down or right at random
def LoR():
    return "down" if random.randint(0,1) else "right"
