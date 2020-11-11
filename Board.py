class Board:
    def __innit__(self):
        board = []
        for x in range(10):
            board.append(["~","~","~","~","~","~","~","~","~","~"])
        destroyer = True
        submarine = True
        cruiser = True
        battleship  = True
        aircraftCarrier = True
  
    def getBoard(self):
        return board

    def printBoard(self):
        for x in board:
            print(x)


    def guess(self, r , c):
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
        for x in self.board:
            for y in self.board[x]:
                if self.board[x][y] == "B":
                    count += 1
        if count == 0 and self.battleship:
            self.battleship = False
            return("battleshp sunk")
        count = 0

        for x in self.board:
            for y in self.board[x]:
                if self.board[x][y] == "D":
                    count += 1
        if count == 0 and self.destroyer:
            self.destroyer = False
            return("destroyer sunk")

        for x in self.board:
            for y in self.board[x]:
                if self.board[x][y] == "S":
                    count += 1
        if count == 0 and self.submarine:
            self.submarine = False
            return("submarine sunk")

        for x in self.board:
            for y in self.board[x]:
                if self.board[x][y] == "C":
                    count += 1
        if count == 0 and self.cruiser:
            self.cruiser = False
            return("cruiser sunk")

        for x in self.board:
            for y in self.board[x]:
                if self.board[x][y] == "A":
                    count += 1
        if count == 0 and self.aircraftCarrier:
            self.aircraftCarrier = False
            return("airfcraft carrier sunk")

        return "nope"

    def placeShip(self, s, x, y):
        if s.getDirection() == "down" and y + s.getLength() > 10:
            return "invalid location"
        elif s.getDirection() == "right" and x + s.getLength() > 10:
            return "invalid location"
        elif x < 0 or y < 0:
            return "invalid location"

        good = True

        if s.getDirection() == "down":
            for a in range(s.getLength()):
                if self.board[y + a - 1][x] != "~":
                    good = False
            if not good:
                return "invalid location"
            else:
                for b in range(s.getLength()):
                    self.board[y + a - 1][x] = s.getType()
                return "changes have been made"

        if s.getDirection() == "right":
            for a in range(s.getLength()):
                if self.board[y][x + a - 1] != "~":
                    good = False
            if not good:
                return "invalid location"
            else:
                for b in range(s.getLength()):
                    self.board[y][x + a - 1] = s.getType()
                return "changes have been made"

            
class gBoard:
    def __innit__(self):
        gB = []
        for x in range(10):
            gB.append(["~","~","~","~","~","~","~","~","~","~"])

    def printGB(self):
        for x in gB:
            print(x)
        
    def doGuess(self, r, c, target):
        g = target.guess(r, c)
        if g == "miss":
            gB[c][r] = "O"
            return
        elif g ==  "out of bounds" or g == "already guessed":
            return
        else:
            gB[c][r] = "x"

    def getGB(self):
        return gB
            
