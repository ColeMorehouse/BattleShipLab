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
        if r < 0 or r > 9 or c < 0 or c > 9:#out of bounds
            return "out of bounds"
        if self.board[r][c] == "h" or self.board[r][c] == "m":#already guessed
            return "already guessed"
        if self.board[r][c] != "~":#hit
            self.board[r][c] = "h"
            if self.checkIfSunk() == "nope":#hit and not sunk
                return "hit"
            else:#hit and sunk
                return self.checkIfSunk()
        else:#miss
            self.board[r][c] = "m"
            return "miss"

    def checkIfSunk(self):
        count = 0

        #check for battlship
        for x in self.board:
            for y in self.board[x]:
                if self.board[x][y] == "B":
        if count == 0 and self.battleship:
            self.battleship = False
            return("battleship sunk")
        count = 0

        #check for destroyer
        for x in self.board:
            for y in self.board[x]:
                if self.board[x][y] == "D":
                    count += 1
        if count == 0 and self.destroyer:
            self.destroyer = False
            return("destroyer sunk")

        #check for submarine
        for x in self.board:
            for y in self.board[x]:
                if self.board[x][y] == "S":
                    count += 1
        if count == 0 and self.submarine:
            self.submarine = False
            return("submarine sunk")

        #check for cruiser
        for x in self.board:
            for y in self.board[x]:
                if self.board[x][y] == "C":
                    count += 1
        if count == 0 and self.cruiser:
            self.cruiser = False
            return("cruiser sunk")

        #check for aircraft Carrier
        for x in self.board:
            for y in self.board[x]:
                if self.board[x][y] == "A":
                    count += 1
        if count == 0 and self.aircraftCarrier:
            self.aircraftCarrier = False
            return("airfcraft carrier sunk")

        return "nope"

    def placeShip(self, shipType, x, y):
        return
