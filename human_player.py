import board
import random

class HumanPlayer:

    def __init__(self, id):
        self.id = id

    def getMove(self, board):
        '''returns the next move for the given board'''
        print(board)
        move = input("your move (give number between 0 and 8)? ")
        return int(move)
