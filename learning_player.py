import board
import random

'''exploration - threshhold above which we do exploration, and below which we do exploitation
    discount - factor by which we devalue future rewards compared to immediate rewards'''
class LearningPlayer:

    

    def __init__(self, discount, exploration, learningRate, id, useSymmetryReduction=True):
        self.discount = discount
        self.exploration = exploration
        self.learningRate = learningRate
        self.valueFunction = dict()
        self.id = id
        '''determines whether we use sets of boards or single boards as keys in the valueFunction'''
        self.useSymmetryReduction = useSymmetryReduction


    def getMove(self, board):
        '''returns the next move for the given board'''
        if(self.exploration <= random.random() ):
           return self.computeMove(board)
        else:
            return self.getRandomMove(board)

    def incorporateReward(self, reward, gameHistory):
        '''applies the reward to the observed gameHistory. 
            There, the reward is discounted, and the update of the value function is dampened by the learningRate'''
        for board in reversed(gameHistory):
            value = self.learningRate * (self.discount * reward - self.getValue(board))
            self.setValue(board, value)
            reward = self.getValue(board)

    # def incorporateReward(self, reward, gameHistory):
    #     '''applies the reward to the observed gameHistory. 
    #         There, the reward is discounted, and the update of the value function is dampened by the learningRate'''
    #     for state in reversed(gameHistory):
    #         stateRep = self.getRepresentatives(state)
    #         if not self.valueFunction.get(stateRep, None):
    #             self.valueFunction[stateRep] = 0
    #         self.valueFunction[stateRep] = self.learningRate * (self.discount * reward - self.valueFunction[stateRep])
    #         reward = self.valueFunction[stateRep] 

    def getRepresentatives(self, board):
        '''returns a representative of the given board.
            If we are using symmetry reduction, the representative is a set containing all board we consider equal to the given one.
            OIf we are not using symmetry reduction, the representative is the given board itself'''
        if self.useSymmetryReduction:
            result = [board]
            for i in range(3):
                result.append(result[-1].getClockwiseRotatedBoard())
            return frozenset(result)
        else:
            return board

    def getRandomMove(self, board):
        '''returns a random possible move'''
        return random.choice(board.getPossibleMoves())

    def getValue(self, board):
        '''returns the value of the given board. 
            Makes sure to access the value function through the representatives of the board.'''
        stateRep = self.getRepresentatives(board)
        return self.valueFunction.get(stateRep, 0)
    
    def setValue(self, board, v):
        '''sets the value of the representative of the given board to the given value v'''
        stateRep = self.getRepresentatives(board)
        self.valueFunction[stateRep] = v

    def computeMove(self, board):
        '''computes the best possible move for the given board, according to the players current value function'''
        moves = board.getPossibleMoves()
        random.shuffle(moves)
        return max(moves, key=lambda m: self.getValue(board.apply(m, self.id)))
    
    def loadValueFunction(self, path):
        '''loads the value frunction from the file with the given path'''

    def saveValueFunction(self, path):
        '''saves the value function to the file at the given path, overriding any previous contents'''

    def getMovesValueFunctions(self, board):
        '''returns a list of tuples with possible moves and the moves value, sorted by their value'''
        moves = board.getPossibleMoves()
        result= [(m, self.getValue(board.apply(m, self.id))) for m in moves]
        result.sort(key=lambda t: t[1], reverse=True)
        return result


