from Board import Board
from Ships import ships
class Player:
    def __init__(self, b1, b2):
        self.board1 = b1
        self.board2 = b2

    #This just picks for the player (used for testing)
    def autoDraft(self):
        self.board1.placeShip(ships("D", "right"), 0, 0)
        self.board1.placeShip(ships("S", "right"), 0, 1)
        self.board1.placeShip(ships("C", "right"), 0, 2)
        self.board1.placeShip(ships("B", "right"), 0, 3)
        self.board1.placeShip(ships("A", "right"), 0, 4)


    #This is the main board setup methof
    def setUpBoard(self):
        self.board1.printBoard()
        check = False
        #while check is false
        while not check:
            ddirect = input("Enter direction of Destroyer: ")
            #checks what direction it is
            if ddirect == "right" or ddirect == "down":
                dest = ships("D", ddirect)
                dposx = input("Enter x coordinate of Destroyer: ")
                dposy = input("Enter y coordinate of Destroyer: ")
                #if it is an improper location
                if self.board1.placeShip(dest,dposx, dposy) != "invalid location":
                    check = True
                else:
                    print("invalid location")

        self.board1.printBoard()
        check = False
        #while check is false
        while not check:
            sdirect = input("Enter direction of Submarine: ")
            #checks what direction it is
            if sdirect == "right" or sdirect == "down":
                sub = ships("S",sdirect)
                sposx = input("Enter x coordinate of Submarine: ")
                sposy = input("Enter y coordinate of Submarine: ")
                #If the location is invalid
                if self.board1.placeShip(sub,sposx, sposy) != "invalid location":
                    check = True
                else:
                    print("invalid location")

        self.board1.printBoard()
        check = False
        #while check is false
        while not check:
            cdirect = input("Enter direction of Cruiser: ")
            # checks what direction it is
            if cdirect == "right" or cdirect == "down":
                cruise = ships("C",cdirect)
                cposx = input("Enter x coordinate of Cruiser: ")
                cposy = input("Enter y coordinate of Cruiser: ")
                # If the location is invalid
                if self.board1.placeShip(cruise,cposx, cposy) != "invalid location":
                    check = True
                else:
                    print("invalid location")

        self.board1.printBoard()
        check = False
        #while check is false
        while not check:
            bdirect = input("Enter direction of BattleShip: ")
            # checks what direction it is
            if bdirect == "right" or bdirect == "down":
                battle = ships("B", bdirect)
                bposx = input("Enter x coordinate of BattleShip: ")
                bposy = input("Enter y coordinate of BattleShip: ")
                # If the location is invalid
                if self.board1.placeShip(battle, bposx, bposy) != "invalid location":
                    check = True
                else:
                    print("invalid location")

        self.board1.printBoard()
        check = False
        # while check is false
        while not check:
            adirect = input("Enter direction of Aircraft Carrier: ")
            # checks what direction it is
            if adirect == "right" or adirect == "down":
                aircraft = ships("A", adirect)
                aposx = input("Enter x coordinate of Aircraft Carrier: ")
                aposy = input("Enter y coordinate of Aircraft Carrier: ")
                # If the location is invalid
                if self.board1.placeShip(aircraft, aposx, aposy) != "invalid location":
                    check = True
                else:
                    print("invalid location")

    #Guesses a space on the AI board
    def guessSpace(self, aiBoard):
        x = input("enter an x value: ")
        y = input("enter an y value: ")
        strRet = aiBoard.guess(y,x)
        # If the location is invalid
        if strRet == "out of bounds" or strRet == "already guessed":
            print(strRet)
            return self.guessSpace(aiBoard)
        else:
            self.board2.doGuess(y,x,aiBoard)
            print(strRet)

    #Accessor method for the first board
    def getB1(self):
        return self.board1

    #Accessor method for the second board
    def getGb(self):
        return self.board2
