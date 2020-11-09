from Board import Board
from Ships import Ships

class Player:
    def __init__(self, b1, b2):
        self.board1 = b1
        self.board2 = b2

    def setUpBoard(self):
        ddirect = input("Enter direction of Destroyer: ")
        dest = Ship("D", ddirect)
        dposx = input("Enter x coordinate of Destroyer: ")
        dposy = input("Enter y coordinate of Destroyer: ")
        placeShip(dest,dposx, dposy)
        
        sdirect = input("Enter direction of Submarine: ")
        sub = Ship("S",sdirect)
        sposx = input("Enter x coordinate of Submarine: ")
        sposy = input("Enter y coordinate of Submarine: ")
        placeShip(sub,sposx, sposy)
        
        cdirect = input("Enter direction of Cruiser: ")
        cruise = Ship("C",cdirect)
        cposx = input("Enter x coordinate of Cruiser: ")
        cposy = input("Enter y coordinate of Cruiser: ")
        placeShip(cruise,cposx, cposy)


    def recieveGuess(self, row, column):
        answer = guess(row, column)
        return answer

    def guessSpace(self):
        row = input("Enter row of guess: ")
        column = input("Enter column of guess: ")
        listGuess = {row, column}
        return listGuess
