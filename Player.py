from Board import Board
from Ships import ships

class Player:
    def __init__(self, b1, b2):
        self.board1 = b1
        self.board2 = b2

    def setUpBoard(self):
        ddirect = input("Enter direction of Destroyer: ")
        dest = ships("D", ddirect)
        dposx = input("Enter x coordinate of Destroyer: ")
        dposy = input("Enter y coordinate of Destroyer: ")
        self.board1.placeShip(dest,dposx, dposy)

        sdirect = input("Enter direction of Submarine: ")
        sub = ships("S",sdirect)
        sposx = input("Enter x coordinate of Submarine: ")
        sposy = input("Enter y coordinate of Submarine: ")
        self.board1.placeShip(sub,sposx, sposy)

        cdirect = input("Enter direction of Cruiser: ")
        cruise = ships("C",cdirect)
        cposx = input("Enter x coordinate of Cruiser: ")
        cposy = input("Enter y coordinate of Cruiser: ")
        self.board1.placeShip(cruise,cposx, cposy)

        bdirect = input("Enter direction of BattleShip: ")
        battle = ships("B", bdirect)
        bposx = input("Enter x coordinate of BattleShip: ")
        bposy = input("Enter y coordinate of BattleShip: ")
        self.board1.placeShip(battle, bposx, bposy)

        adirect = input("Enter direction of Aircraft Carrier: ")
        aircraft = ships("C", cdirect)
        aposx = input("Enter x coordinate of Aircraft Carrier: ")
        aposy = input("Enter y coordinate of Aircraft Carrier: ")
        self.board1.placeShip(aircraft, aposx, aposy)


    def recieveGuess(self, row, column):
        answer = self.board1.guess(row, column)
        return answer

    def guessSpace(self):
        row = input("Enter row of guess: ")
        column = input("Enter column of guess: ")
        listGuess = {row, column}
        return listGuess
