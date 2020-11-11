from board import board
from ships import ships

class Player:
    def __init__(self, b1, b2):
        self.board1 = b1
        self.board2 = b2

    def setUpBoard(self):
        
        ddirect = input("Enter direction of Destroyer: ")
        if (ddirect != "down" ) or (ddirect != "right"):
            print("Not valid direction! Only down or right from starting spot")
        ddirect = input("Enter direction of Destroyer: ")
        dest = Ship("D", ddirect)
        dposx = input("Enter x coordinate of Destroyer: ")
        dposy = input("Enter y coordinate of Destroyer: ")
        b1.placeShip(dest,dposx, dposy)

        sdirect = input("Enter direction of Submarine: ")
        if (sdirect != "down" ) or (sdirect != "right"):
            print("Not valid direction! Only down or right from starting spot")
        sdirect = input("Enter direction of Submarine: ")
        sub = Ship("S",sdirect)
        sposx = input("Enter x coordinate of Submarine: ")
        sposy = input("Enter y coordinate of Submarine: ")
        b1.placeShip(sub,sposx, sposy)

        cdirect = input("Enter direction of Cruiser: ")
        if (cdirect != "down" ) or (cdirect != "right"):
            print("Not valid direction! Only down or right from starting spot")
        cdirect = input("Enter direction of Cruiser: ")
        cruise = Ship("C",cdirect)
        cposx = input("Enter x coordinate of Cruiser: ")
        cposy = input("Enter y coordinate of Cruiser: ")
        b1.placeShip(cruise,cposx, cposy)

        bdirect = input("Enter direction of BattleShip: ")
        if (bdirect != "down" ) or (bdirect != "right"):
            print("Not valid direction! Only down or right from starting spot")
        bdirect = input("Enter direction of BattleShip: ")
        battle = Ship("B", bdirect)
        bposx = input("Enter x coordinate of BattleShip: ")
        bposy = input("Enter y coordinate of BattleShip: ")
        b1.placeShip(battle, bposx, bposy)

        adirect = input("Enter direction of Aircraft Carrier: ")
        if (adirect != "down" ) or (adirect != "right"):
            print("Not valid direction! Only down or right from starting spot")
        adirect = input("Enter direction of Aircraft Carrier: ")
        aircraft = Ship("C", adirect)
        aposx = input("Enter x coordinate of Aircraft Carrier: ")
        aposy = input("Enter y coordinate of Aircraft Carrier: ")
        b1.placeShip(aircraft, aposx, aposy)


    def recieveGuess(self, row, column):
        answer = b1.guess(row, column)
        return answer

    def guessSpace(self):
        row = input("Enter row of guess: ")
        column = input("Enter column of guess: ")
        listGuess = {row, column}
        return listGuess
