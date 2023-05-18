

def boards2str(boards):
    result = ""
    for b in boards:
        result += str(b) + '\n'
    return result

class Board:
    def __init__(self, ids=['X', 'O'], NONE='_'):
        self.entries = tuple([NONE] * 9)
        self.ids = ids
        self.NONE = NONE

    def copy(self):
        copy = Board()
        copy.entries = self.entries
        return copy

    def getValue(self, x, y):
        return self.entries[y * 3 + x]
    
    def putValue(self, x, y, v):
        #self.entries[y * 3 + x] = v
        self.entries = self.entries[:y * 3 + x] + (v,) + self.entries[y * 3 + x + 1:] 


    def getPossibleMoves(self):
        return [x for x in range(9) if self.entries[x] == self.NONE]
    
    def getClockwiseRotatedBoard(self):
        '''creates a new board rotated by 90° in clockwise direction'''
        result = self.copy()
        result.entries = (result.entries[6], result.entries[3], result.entries[0], \
                            result.entries[7], result.entries[4], result.entries[1], \
                            result.entries[8], result.entries[5], result.entries[2])
        return result

    
    def apply(self, move, value):
        '''applies the given move to the current board'''
        if self.entries[move] != self.NONE or value not in self.ids:
            raise ValueError
        else:
            copy = Board()
            copy.entries = self.entries[:move] + (value,) + self.entries[move + 1:] 
            return copy
        
    def hasWinner(self):
        '''determines whether the game with the given board is finished or not'''
        return self.getWinner() != self.NONE or self.entries.count(self.NONE) == 0 
        

    def getWinner(self):
        '''determines the id of the winner for the given board. Returns 0 if there is a tie'''
        for id in self.ids:
            # check the diagonals
            if (id == self.getValue(0, 0) and id == self.getValue(1, 1) and id == self.getValue(2, 2)) or \
                    (id == self.getValue(2, 0) and id == self.getValue(1, 1) and id == self.getValue(0, 2)):
                    return id
            # check the vertical and horizontal lines
            for i in range(3):
                if (id == self.getValue(0, i) and id == self.getValue(1, i) and id == self.getValue(2, i)) or \
                    (id == self.getValue(i, 0) and id == self.getValue(i, 1) and id == self.getValue(i, 2)):
                    return id
        # nothing else matched, apparently there is now winner
        return self.NONE

    def __str__(self):
        result = ""
        for y in range(3):
            for x in range(3):
                v = self.getValue(x, y)
                result += " " + v + " "
            result += '\n'
        return result
    
    def __eq__(self, other):
        if isinstance(other, Board):
            return other.entries == self.entries
        else:
            return False
        
    def __hash__(self):
        return hash(self.entries)



