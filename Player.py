from Board import Board
from Ships import Ships

class Player:
    def __init__(self, b1, b2):
        self.board1 = b1
        self.board2 = b2

    def placeShips(self, ship, row, col):
        dict = {
            "n": row > ship.getLength() and row <= 9,
            "e": col <= 10 - ship.getLength() and col <= 0,
            "s": row <= 10 - ship.getLength() and row <= 0,
            "w": col > ship.getLength()-1 and col <= 9
        }
        if ship.getType() == "D":
            pass

        if ship.getType() == "S" or ship.type == "C":
            pass

        if ship.getType() == "B":
            pass

        if ship.getType() == "A":
            pass

    def recieveGuess(self, row, column):
        answer = self.guess(row, column)
        return answer

    def guessSpace(self):
        row = input("Enter row of guess: ")
        column = input("Enter column of guess: ")
        listGuess = {row, column}
        return listGuess
