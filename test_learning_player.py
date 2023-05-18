import unittest
from learning_player import LearningPlayer
from board import Board
import board
import ipdb



class TestLearningPlayer(unittest.TestCase):


    def test_getRepresentatives(self):
        b = Board()
        lp = LearningPlayer(0.9, 0.3, 0.2, 'X', True)
        b.putValue(0,0, 'X')
        b.putValue(1,1, 'O')

        b1 = Board()
        b1.putValue(2,0, 'X')
        b1.putValue(1,1, 'O')

        b2 = Board()
        b2.putValue(2,2, 'X')
        b2.putValue(1,1, 'O')

        b3 = Board()
        b3.putValue(0,2, 'X')
        b3.putValue(1,1, 'O')

        self.assertEqual(lp.getRepresentatives(b), frozenset([b, b1, b2, b3]))
        self.assertEqual(lp.getRepresentatives(b1), frozenset([b, b1, b2, b3]))

        lp = LearningPlayer(0.9, 0.3, 0.2, 'X', False)
        self.assertEqual(lp.getRepresentatives(b), b)
        self.assertNotEqual(lp.getRepresentatives(b), b1)

    def test_incorporateReward0(self):
        b = Board()
        b1 = Board()
        b1.putValue(1,0, 'X')
        # we set exploration to -1 to deactivate it
        lp = LearningPlayer(0.9, -1.0, 0.2, 'X', True)

        lp.incorporateReward(1, [b, b1])
        self.assertTrue(lp.getMove(b) in [1, 3, 5, 7], "After getting positive feedback "  
                "the player should attempt to reach a board "
                "considered equal to the observed board b1")
        
        lp = LearningPlayer(0.9, -1.0, 0.2, 'X', False)
        lp.incorporateReward(1, [b, b1])
        self.assertEqual(lp.getMove(b), 1, "After getting positive feedback "  
                "the player should attempt to reach the previously observed board")

    def test_incorporateReward1(self):
        b0 = Board()
        b1 = Board()
        b1.putValue(1,0, 'X')
        # we set exploration to -1 to deactivate it
        lp = LearningPlayer(0.9, -1.0, 0.2, 'X', True)

        #ipdb.set_trace()
        lp.incorporateReward(-1, [b0, b1])
        self.assertTrue(lp.getMove(b0) not in [1, 3, 5, 7], "After getting negative feedback "  
                "the player should attempt to avoid a board "
                "considered equal to the observed board b1")
        self.assertTrue(lp.getValue(b0.apply(1, lp.id)) < 0)

        
        lp = LearningPlayer(0.9, -1.0, 0.2, 'X', False)
        lp.incorporateReward(-1, [b0, b1])
        self.assertNotEqual(lp.getMove(b0), 1, "After getting negative feedback "  
                "the player should avoid the previously observed board")




if __name__ == '__main__':
    unittest.main()
