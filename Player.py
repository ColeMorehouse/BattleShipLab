from Board import Board
from Ships import Ships

class Player:
    def __init__(self, b1, b2):
        self.board1 = b1
        self.board2 = b2

    def placeShips(self, ship, row, col):
        dict = {
            "down": row <= 10 - ship.getLength() and row >= 0,
            "right": col <= 10 - ship.getLength() and col >= 0
        }
        if ship.getType() == "D":
            
        if ship.getType() == "S" or ship.type == "C":

        if ship.getType() == "B":

        if ship.getType() == "A":


    def recieveGuess(self, row, column):
        answer = guess(row, column)
        return answer

    def guessSpace(self):
        row = input("Enter row of guess: ")
        column = input("Enter column of guess: ")
        listGuess = {row, column}
        return listGuess
