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
            if board.placeShip(ship, random.randint(1, 9), random.randint(1, 9)) == "invalid location":
                continue
            else:
                break
    def getBoard(self):
        return self.board1




def LoR():
    return "down" if random.randint(0,1) else "right"


