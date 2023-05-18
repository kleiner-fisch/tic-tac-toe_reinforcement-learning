# tic-tac-toe_reinforcement-learning
Simple module to train a TicTacToe AI-player using reinforcement learning.

To get started download, start interactive python mode and from the root directory of this project execute the code below. That will train the AI-player with 10000 games against a random player. Then the trained AI-player will play 1000 games against a random player. The win rate will not be great, but at least it should be > 50%.

```python
from tic_tac_toe import TicTacToe    
from learning_player import LearningPlayer
from random_player import RandomPlayer
p0 = LearningPlayer(0.9, 0.3, 0.2, 'X', True)
p1 = RandomPlayer('O')
game = TicTacToe(players=[p0, p1])
game.train(10000)
p0.exploration = 0
game.playN(1000)
print(game.computeWinRate())
```


Some inspiration (in particular the learning formula) is taken from https://towardsdatascience.com/reinforcement-learning-implement-tictactoe-189582bea542
