from Board import Board
from Ships import ships
import random

class ai:

    def keepPlacing(self, ship):
        while (True):
            if (self.Board.placeShip(self.ship, random.randint(0, 9), random.randint(0, 9)) == "Invalid Guess"):
                continue
            else:
                break

    def __init__(self, b1, b2):
        board1 = b1
        board2 = b2
        D = ships('D', LoR())
        S = ships('S', LoR())
        C = ships('C', LoR())
        B = ships('B', LoR())
        A = ships('A', LoR())
        self.keepPlacing(D)
        self.keepPlacing(S)
        self.keepPlacing(C)
        self.keepPlacing(B)
        self.keepPlacing(A)







def LoR():
    return "left" if random.randint(0,1) else "right"


