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


    def guess(self, r , c):
        if self.board[r][c] is not "~":
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


