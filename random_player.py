import board
import random

class RandomPlayer:

    def __init__(self, id):
        self.id = id

    def getMove(self, board):
        '''returns the next move for the given board'''
        return self.getRandomMove(board)

    def getRandomMove(self, board):
        '''returns a random possible move'''
        return random.choice(board.getPossibleMoves())