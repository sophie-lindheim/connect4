import unittest
import numpy as np
from connect4.c4_class import C4Game


class CheckTestCase(unittest.TestCase):
    """Unittest to test the check_winner function.

       In this test the check winner function of the econnect4 game is tested. 4 different win cases are tested;
       winning by putting 4 stones in a row, in a column and each options in a diagonal. Each of these winning cases
       will also be checked for each player; one, two and the computer. The first four methods tests if the game
       terminates with end_game variable value True after player 2, which is a real player, has won by putting 4 stones
       in a row. The second method tests, if player 1, which is a real player, has won by
       putting 4 stones in a row. The third method tests if player 1, which is a real player, has won by putting 4
       stones in a column. The fourth tests if

       """

    def setUp(self):
        self.actual_player = 2
        self.game_mode = 2
        self.end_game = None
        self.table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 0],
                               [0, 1, 0, 2, 0, 0, 0], [0, 1, 0, 2, 0, 0, 0], [0, 1, 1, 2, 0, 0, 0]])

    # First Round of winning case: "Win in a row"

    # checking output if player 2's winning has triggered the end_game variable to be True:
    def test_player2_won_row(self):
        C4Game.check_winner(self)
        self.assertTrue(self.end_game, msg='Player 2 has not won!')

    # checking output if player 1's winning in a row has triggered the end_game variable to be True:
    def test_player1_won_row(self):
        self.actual_player = 1
        self.table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0],
                               [0, 1, 0, 2, 0, 0, 0], [0, 1, 0, 2, 0, 0, 0], [0, 1, 1, 2, 0, 0, 0]])
        C4Game.check_winner(self)
        self.assertTrue(self.end_game, msg='Player 1 has not won!')

    # checking output if computer's winning in a row has triggered the end_game variable to be True:
    def test_computer_won_row(self):
        self.game_mode = 1
        self.table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2],
                               [0, 1, 1, 2, 0, 0, 2], [0, 1, 2, 2, 1, 0, 2], [0, 1, 1, 2, 1, 1, 2]])
        C4Game.check_winner(self)
        self.assertTrue(self.end_game, msg='Computer has not won!')

    # Second Round of winning case: "Win in a column"

    # checking output if player 1's winning has triggered the end_game variable to be True:
    def test_player1_won_column(self):
        self.actual_player = 1
        self.table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 2, 0, 0], [1, 1, 1, 1, 2, 0, 0]])
        C4Game.check_winner(self)
        self.assertTrue(self.end_game, msg='Player 1 has not won!')

    # checking output if player 2's winning has triggered the end_game variable to be True:
    def test_player2_won_column(self):
        self.table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 2, 2, 2, 2], [1, 1, 1, 2, 1, 1, 1]])
        C4Game.check_winner(self)
        self.assertTrue(self.end_game, msg='Player 1 has won again!')

    # checking output if computer's winning has triggered the end_game variable to be True:
    def test_computer_won_column(self):
        pass

    # Third Round of winning case: "Win in a diagonal"

    # checking output if player 1's winning has triggered the end_game variable to be True:
    def test_player1_won_diagonal(self):
        pass

    # checking output if player 2's winning has triggered the end_game variable to be True:
    def test_player2_won_diagonal(self):
        pass

    # checking output if computer's winning has triggered the end_game variable to be True:
    def test_computer_won_diagonal(self):
        pass

    # Fourth Round of winning case: "Win in the other diagonal"

    # checking output if player 1's winning has triggered the end_game variable to be True:
    def test_player1_won_diagonal2(self):
        pass

    # checking output if player 2's winning has triggered the end_game variable to be True:
    def test_player2_won_diagonal2(self):
        pass

    # checking output if computer's winning has triggered the end_game variable to be True:
    def test_computer_won_diagonal2(self):
        pass


if __name__ == '__main__':
    unittest.main()
