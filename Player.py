from Board import Board
from Ships import ships

class Player:
    def __init__(self, b1, b2):
        self.board1 = b1
        self.board2 = b2

    def setUpBoard(self):

        check = False
        while not check:
            ddirect = input("Enter direction of Destroyer: ")
            if ddirect == "right" or ddirect == "down":
                dest = ships("D", ddirect)
                dposx = input("Enter x coordinate of Destroyer: ")
                dposy = input("Enter y coordinate of Destroyer: ")
                if self.board1.placeShip(dest,dposx, dposy) != "invalid location":
                    check = True

        check = False
        while not check:
            sdirect = input("Enter direction of Submarine: ")
            if sdirect == "right" or sdirect == "down":
                sub = ships("S",sdirect)
                sposx = input("Enter x coordinate of Submarine: ")
                sposy = input("Enter y coordinate of Submarine: ")
                if self.board1.placeShip(sub,sposx, sposy) != "invalid location":
                    check = True

        check = False
        while not check:
            cdirect = input("Enter direction of Cruiser: ")
            if cdirect == "right" or cdirect == "down":
                cruise = ships("C",cdirect)
                cposx = input("Enter x coordinate of Cruiser: ")
                cposy = input("Enter y coordinate of Cruiser: ")
                if self.board1.placeShip(cruise,cposx, cposy) != "invalid location":
                    check = True

        check = False
        while not check:
            bdirect = input("Enter direction of BattleShip: ")
            if bdirect == "right" or bdirect == "down":
                battle = ships("B", bdirect)
                bposx = input("Enter x coordinate of BattleShip: ")
                bposy = input("Enter y coordinate of BattleShip: ")
                if self.board1.placeShip(battle, bposx, bposy) != "invalid location":
                    check = True

        check = False
        while not check:
            adirect = input("Enter direction of Aircraft Carrier: ")
            if adirect == "right" or adirect == "down":
                aircraft = ships("A", adirect)
                aposx = input("Enter x coordinate of Aircraft Carrier: ")
                aposy = input("Enter y coordinate of Aircraft Carrier: ")
                if self.board1.placeShip(aircraft, aposx, aposy) != "invalid location":
                    check = True


    def recieveGuess(self, row, column):
        check = False
        while not check:
            answer = self.board1.guess(row, column)
            if answer == "out of bounds" or answer == "already guessed":
                return answer
            else:
                check = True
        return answer

    def guessSpace(self):
        row = input("Enter row of guess: ")
        column = input("Enter column of guess: ")
        listGuess = {row, column}
        return listGuess

    def getB1(self):
        return self.board1

    def getGb(self):
        return self.board2