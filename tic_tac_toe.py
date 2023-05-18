from board import Board
import random
from learning_player import LearningPlayer
from random_player import RandomPlayer
# import ipdb

'''Simple module to train an AI-player using reinforcement learning.
    Currently 3 player types are supported: the learning player, random player and human player.
    Below a sequence of commands to get started in interactive mode:

from tic_tac_toe import TicTacToe    
from learning_player import LearningPlayer
from random_player import RandomPlayer
p0 = LearningPlayer(0.9, 0.3, 0.2, 'X', True)
p1 = RandomPlayer('O')
game = TicTacToe(players=[p0, p1])
game.train(10000)
p0.exploration = 0
game.playN(1000)
print(game.computeWinRate())'''
class TicTacToe:

    # history
    # players: [p0, p1]
    # currentPlayer: 0 or 1

    def __init__(self, players=[], ids=['X', 'O'], NONE='_'):
        self.history = []
        self.players = players
        self.startingPlayer = 0
        self.ids = ids
        self.NONE=NONE

    def play(self):
        '''plays a single game with the current configuration (no rewards given) and returns the id of winner (or 0 in case of tie) '''
        currentPlayer = self.startingPlayer
        board = Board(self.ids, self.NONE)
        localHistory = [board]
        while not board.hasWinner():
            move = self.players[currentPlayer].getMove(board)
            board = board.apply(move, self.players[currentPlayer].id)
            currentPlayer = 1 - currentPlayer
            localHistory.append(board)
        self.history.append(localHistory)
        return board.getWinner()



    def playN(self, n, startingPlayerChooser=lambda x:random.randint(0,1)):
        '''plays <n> games with the current configuration (no rewards given)
        startingPlayerChooser: int -> int -- a function determining the starting player, given the starting player in the previous round.
                The default function always picks a new random player'''
        self.history = []
        for i in range(n):
            self.startingPlayer = startingPlayerChooser(self.startingPlayer)
            self.play()



    def showHistory(self):
        result = ""
        for gameHistory in self.history:
            for state in gameHistory:
                result += str(state)
                result += '__________\n'
            result += '==========================\n'
        return result



    def train(self, n, startingPlayerChooser=lambda x:random.randint(0,1)):
        '''do <n> games with rewards given after each game
        startingPlayer: int -> int -- a function determining the starting player, given the starting player in the previous round'''
        self.history = []
        for i in range(n):
            self.startingPlayer = startingPlayerChooser(self.startingPlayer)
            winner = self.play()
            self.giveRewards(winner, self.history[-1])

    def giveRewards(self, winner, gameHistory):
        for p in self.players:
            if isinstance(p, LearningPlayer):
                if p.id == winner:
                    reward = 1
                elif winner == 0:
                    reward = 0.1
                else:
                    reward = 0
                p.incorporateReward(reward, gameHistory)       

    def computeWinRate(self):
        '''computes the win rate and returns it as a directory: id -> (%win, %tie, %loss)'''
        numGames = len(self.history)
        if numGames ==0:
            return dict()
        wins = [gameHistory[-1].getWinner() for gameHistory in self.history]
        result = dict()
        for id in self.ids:
            result[id] = {'wins' : wins.count(id) / numGames, 'ties' : wins.count(self.NONE) / numGames}
        return result




