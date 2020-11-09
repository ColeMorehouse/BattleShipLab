from Board import Board
from Ships import Ships

class Player:
    def __init__(self, b1, b2):
        self.board1 = b1
        self.board2 = b2

    def setUpBoard(self):
        ddirect = input("Enter direction of Destroyer: ")
        dest = Ship("D", up, ddirect)


    def recieveGuess(self, row, column):
        answer = guess(row, column)
        return answer

    def guessSpace(self):
        row = input("Enter row of guess: ")
        column = input("Enter column of guess: ")
        listGuess = {row, column}
        return listGuess
