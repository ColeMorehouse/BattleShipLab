from Board import Board
from Ships import ships
import random
from Player import Player
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
from ai import ai

class aiChild(ai):

    def changeBoard(self, b1,b2):
        self.board1 = b1
        self.board2 = b2