from Ships import ships

class Board:
    def __init__(self):
        self.board = []
        for x in range(10):
            self.board.append(["~","~","~","~","~","~","~","~","~","~"])
        self.destroyer = True
        self.submarine = True
        self.cruiser = True
        self.battleship  = True
        self.aircraftCarrier = True
  
    def getBoard(self):
        return self.board

    def checkWin(self):
        count = 0
        for y in self.board:
            for x in y:
                if x == "~" or x == "m" or x == "h":
                    continue
                else:
                    count += 1
        if count > 0:
            return False
        else:
            return True


    def printBoard(self):
        for x in self.board:
            print(x)

    def guess(self, r , c):#NOTE: THIS IS y,x, NOT x,y
        r = int(r)
        c = int(c)
        if r < 0 or r > 9 or c < 0 or c > 9:
            return "out of bounds"
        if self.board[r][c] == "h" or self.board[r][c] == "m":
            return "already guessed"
        if self.board[r][c] != "~":
            self.board[r][c] = "h"
            if self.checkIfSunk() == "nope":
                return "hit"
            else:
                return self.checkIfSunk()
        else:
            self.board[r][c] = "m"
            return "miss"

    def checkIfSunk(self):
        count = 0
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == "B":
                    count += 1
        if count == 0 and self.battleship:
            self.battleship = False
            return("battleship sunk")
        count = 0

        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == "D":
                    count += 1
        if count == 0 and self.destroyer:
            self.destroyer = False
            return("destroyer sunk")

        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == "S":
                    count += 1
        if count == 0 and self.submarine:
            self.submarine = False
            return("submarine sunk")

        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == "C":
                    count += 1
        if count == 0 and self.cruiser:
            self.cruiser = False
            return("cruiser sunk")

        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == "A":
                    count += 1
        if count == 0 and self.aircraftCarrier:
            self.aircraftCarrier = False
            return("airfcraft carrier sunk")

        return "nope"

    def placeShip(self, s, x, y):
        x = int(x)
        y = int(y)
        if s.getDirection() == "down" and y + s.getLength() - 1 > 9:
            return "invalid location"
        elif s.getDirection() == "right" and x + s.getLength() - 1 > 9:
            return "invalid location"
        elif x < 0 or y < 0:
            return "invalid location"

        good = True

        if s.getDirection() == "down":
            for a in range(s.getLength()):
                if self.board[y + a][x] != "~":
                    good = False
            if not good:
                return "invalid location"
            else:
                for b in range(s.getLength()):
                    self.board[y + b][x] = s.getType()
                return "changes have been made"

        if s.getDirection() == "right":
            for a in range(s.getLength()):
                if self.board[y][x + a] != "~":
                    good = False
            if not good:
                return "invalid location"
            else:
                for b in range(s.getLength()):
                    self.board[y][x + b] = s.getType()
                return "changes have been made"

            
class gBoard:
    def __init__(self, bE):
        self.targetBoard = bE
        self.gB = []
        for x in range(10):
            self.gB.append(["~","~","~","~","~","~","~","~","~","~"])

    def doGuess(self, r, c, board):
        r = int(r)
        c = int(c)
        self.gB[r][c] = board.getBoard()[r][c]

    def getGb(self):
        return self.gB

    def printGb(self):
        for x in self.gB:
            print(x)
