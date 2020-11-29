from Ships import ships

class Board:
    def __init__(self):
        self.board = []
        #traverses from 1 to 10, builds the board
        for x in range(10):
            self.board.append(["~","~","~","~","~","~","~","~","~","~"])
        self.destroyer = True
        self.submarine = True
        self.cruiser = True
        self.battleship  = True
        self.aircraftCarrier = True

    #accessor for the board
    def getBoard(self):
        return self.board

    #checks if someone has won
    def checkWin(self):
        count = 0
        #Traverses the entire array
        for y in self.board:
            for x in y:
                #makes sure there aren't any ships yet
                if x == "~" or x == "m" or x == "h":
                    continue
                else:
                    count += 1
        #If there are any left
        if count > 0:
            return False
        else:
            return True

    #Prints out the board
    def printBoard(self):
        #Traverses the Y-values
        for x in self.board:
            print(x)

    #Guesses on the board
    def guess(self, r , c):#NOTE: THIS IS y,x, NOT x,y
        r = int(r)
        c = int(c)
        #checks if it is valid
        if r < 0 or r > 9 or c < 0 or c > 9:
            return "out of bounds"
        #checks if it's already guessed
        if self.board[r][c] == "h" or self.board[r][c] == "m":
            return "already guessed"
        #if the board at that index is empty
        if self.board[r][c] != "~":
            self.board[r][c] = "h"
            #checks if it has not been sunk
            if self.checkIfSunk() == "nope":
                return "hit"
            else:
                return self.checkIfSunk()
        else:
            self.board[r][c] = "m"
            return "miss"

    #checks if the ship is sunk
    def checkIfSunk(self):
        count = 0
        #traverses the entire array
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                #The tally for the ship
                if self.board[x][y] == "B":
                    count += 1
        #if it has been sunk
        if count == 0 and self.battleship:
            self.battleship = False
            return("battleship sunk")
        count = 0
        #traverses the entire array
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                # The tally for the ship
                if self.board[x][y] == "D":
                    count += 1
        #if it has been sunk
        if count == 0 and self.destroyer:
            self.destroyer = False
            return("destroyer sunk")
        #traverses the entire array
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                # The tally for the ship
                if self.board[x][y] == "S":
                    count += 1
        #if it has been sunk
        if count == 0 and self.submarine:
            self.submarine = False
            return("submarine sunk")
        #traverses the entire array
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                # The tally for the ship
                if self.board[x][y] == "C":
                    count += 1
        #if it has been sunk
        if count == 0 and self.cruiser:
            self.cruiser = False
            return("cruiser sunk")
        #traverses the entire array
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                # The tally for the ship
                if self.board[x][y] == "A":
                    count += 1
        #if it has been sunk
        if count == 0 and self.aircraftCarrier:
            self.aircraftCarrier = False
            return("airfcraft carrier sunk")

        return "nope"

    #places the ship
    def placeShip(self, s, x, y):
        x = int(x)
        y = int(y)
        #checks if the location is valid
        if s.getDirection() == "down" and y + s.getLength() - 1 > 9:
            return "invalid location"
        elif s.getDirection() == "right" and x + s.getLength() - 1 > 9:
            return "invalid location"
        elif x < 0 or y < 0:
            return "invalid location"

        good = True

        #checks if the location is valid
        if s.getDirection() == "down":
            #traverses the length of the ship
            for a in range(s.getLength()):
                #checks if it is open
                if self.board[y + a][x] != "~":
                    good = False
            #checks if the location is valid
            if not good:
                return "invalid location"
            else:
                #also traverses the length
                for b in range(s.getLength()):
                    self.board[y + b][x] = s.getType()
                return "changes have been made"

        #if it is rightward
        if s.getDirection() == "right":
            #traverses the ship
            for a in range(s.getLength()):
                #if it is empty
                if self.board[y][x + a] != "~":
                    good = False
            #if it is invalid
            if not good:
                return "invalid location"
            else:
                #traverses the ship
                for b in range(s.getLength()):
                    self.board[y][x + b] = s.getType()
                return "changes have been made"

    #toString method
    def toString(self):
        tbr = ""
        #traverses the board, returns it as a string
        for x in self.board:
            tbr+=(str(x)+"\n")
        return tbr


class gBoard:
    def __init__(self, bE):
        self.targetBoard = bE
        self.gB = []
        #from 1 to 10, creates it
        for x in range(10):
            self.gB.append(["~","~","~","~","~","~","~","~","~","~"])

    #guesses on the guess board
    def doGuess(self, r, c, board):
        r = int(r)
        c = int(c)
        self.gB[r][c] = board.getBoard()[r][c]

    #accessor method for gb
    def getGb(self):
        return self.gB

    #prints out the gb
    def printGb(self):
        for x in self.gB:
            print(x)

    #toString method for the gb
    def toString(self):
        tbr = ""
        for x in self.gB:
            tbr += (str(x) + "\n")
        return tbr
