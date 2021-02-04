import unittest
import numpy as np
from c4_class import C4Game


class CheckTestCase(unittest.TestCase):
    """Unittest to test the check_winner function.

       In this test the check winner function of the econnect4 game is tested. Four different win cases are tested;
       winning by putting four stones in a column, in a row and each options in a diagonal. Each of these winning case
       will also be checked for each player options; one, two and the computer. The first four methods tests if the game
       terminates with end_game variable value True after every player has won by putting four stones
       in a row. The second stack of four methods tests if the game terminates with end_game variable value True
       after every player has won by putting four stones in a column. The third and fourth stack of four methods tests
       if every player has won by putting four stones in each ways of a diagonal. All in all there 12 tests to pass.

       """

    def setUp(self):
        """"Setup for the unittest.

        Sets up the test game mode with two "real" players, player 2 in charge and a table where player two is
        winning by 4 stones in a column. The end_game variable needs to be set up with None, since that is the
        boolean variable that needs to be checked each time

        """
        self.actual_player = 2
        self.game_mode = 2
        self.end_game = None
        self.table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 0],
                               [0, 1, 0, 2, 0, 0, 0], [0, 1, 0, 2, 0, 0, 0], [0, 1, 1, 2, 0, 0, 0]])

    # First Round of winning case: "Win in a column"

    # checking output if player 2's winning has triggered the end_game variable to be True:
    def test_player2_won_column(self):
        C4Game.check_winner(self)
        self.assertTrue(self.end_game, msg='Player 2 has not won!')

    # checking output if player 1's winning has triggered the end_game variable to be True:
    def test_player1_won_column(self):
        self.actual_player = 1
        self.table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0],
                               [0, 1, 0, 2, 0, 0, 0], [0, 1, 0, 2, 0, 0, 0], [0, 1, 1, 2, 0, 0, 0]])
        C4Game.check_winner(self)
        self.assertTrue(self.end_game, msg='Player 1 has not won!')

    # checking output if computer's winning has triggered the end_game variable to be True:
    def test_computer_won_column(self):
        self.game_mode = 1
        self.table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2],
                               [0, 1, 1, 2, 0, 0, 2], [0, 1, 2, 2, 1, 0, 2], [0, 1, 1, 2, 1, 1, 2]])
        C4Game.check_winner(self)
        self.assertTrue(self.end_game, msg='Computer has not won!')

    # Second Round of winning case: "Win in a row"

    # checking output if player 1's winning has triggered the end_game variable to be True:
    def test_player1_won_row(self):
        self.actual_player = 1
        self.table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 2, 0, 0], [1, 1, 1, 1, 2, 0, 0]])
        C4Game.check_winner(self)
        self.assertTrue(self.end_game, msg='Player 1 has not won!')

    # checking output if player 2's winning has triggered the end_game variable to be True:
    def test_player2_won_row(self):
        self.table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 2, 2, 2, 2], [1, 1, 1, 2, 1, 1, 1]])
        C4Game.check_winner(self)
        self.assertTrue(self.end_game, msg='Player 2 has not won!!')

    # checking output if computer's winning has triggered the end_game variable to be True:
    def test_computer_won_row(self):
        self.game_mode = 1
        self.table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 2, 2, 0], [0, 0, 1, 2, 2, 2, 2], [1, 1, 1, 2, 1, 1, 1]])
        C4Game.check_winner(self)
        self.assertTrue(self.end_game, msg='Computer has not won!')

    # Third Round of winning case: "Win in a diagonal"

    # checking output if player 1's winning has triggered the end_game variable to be True:
    def test_player1_won_diagonal(self):
        self.actual_player = 1
        self.table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0],
                               [0, 0, 1, 2, 2, 0, 0], [0, 1, 2, 1, 2, 0, 0], [1, 1, 1, 2, 1, 0, 2]])
        C4Game.check_winner(self)
        self.assertTrue(self.end_game, msg='Player 1 has not won!')

    # checking output if player 2's winning has triggered the end_game variable to be True:
    def test_player2_won_diagonal(self):
        self.table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 2, 0, 0, 0],
                               [1, 2, 1, 2, 2, 0, 0], [0, 1, 2, 1, 2, 2, 1], [1, 1, 1, 2, 1, 1, 2]])
        C4Game.check_winner(self)
        self.assertTrue(self.end_game, msg='Player 2 has not won!!')

    # checking output if computer's winning has triggered the end_game variable to be True:
    def test_computer_won_diagonal(self):
        self.game_mode = 1
        self.table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [2, 1, 2, 2, 0, 0, 0],
                               [1, 2, 1, 2, 2, 0, 0], [0, 1, 2, 1, 2, 2, 1], [1, 1, 1, 2, 1, 1, 2]])
        C4Game.check_winner(self)
        self.assertTrue(self.end_game, msg='Computer has not won!')

    # Fourth Round of winning case: "Win in the other diagonal"

    # checking output if player 1's winning has triggered the end_game variable to be True:
    def test_player1_won_diagonal2(self):
        self.actual_player = 1
        self.table = (np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 2, 0, 0, 0],
                   [1, 2, 1, 2, 2, 0, 0], [0, 1, 2, 1, 2, 0, 0], [1, 1, 1, 2, 1, 0, 2]]))
        C4Game.check_winner(self)
        self.assertTrue(self.end_game, msg='Player 1 has not won!')

    # checking output if player 2's winning has triggered the end_game variable to be True:
    def test_player2_won_diagonal2(self):
        np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [2, 0, 1, 1, 0, 0, 0],
                  [1, 2, 1, 2, 2, 0, 0], [0, 1, 2, 1, 2, 0, 0], [1, 1, 1, 2, 1, 0, 2]])
        C4Game.check_winner(self)
        self.assertTrue(self.end_game, msg='Player 2 has not won!!')

    # checking output if computer's winning has triggered the end_game variable to be True:
    def test_computer_won_diagonal2(self):
        self.game_mode = 1
        np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [2, 0, 1, 1, 0, 0, 1],
                  [1, 2, 1, 2, 2, 0, 0], [0, 1, 2, 1, 2, 0, 0], [1, 1, 1, 2, 1, 0, 2]])
        C4Game.check_winner(self)
        self.assertTrue(self.end_game, msg='Computer has not won!')


if __name__ == '__main__':
    unittest.main()
