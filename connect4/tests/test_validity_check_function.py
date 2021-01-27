import unittest
from unittest.mock import patch
import numpy as np
from connect4.c4_class import C4Game


class ValidityTestCase(unittest.TestCase):
    """Unittest to test the validity_check function.

       In this test the validity check function of th econnect4 game is tested. 3 cases are tested, the first
       method tests if the function reacts correctly if an input comes to an already full column.
       The second method tests, if the function reacts correctly if the input is not a valid column letter.
       The third tests is the function changes the right variable to the right value with a valid input.

       """

    def setUp(self):
        self.actual_player = 1
        self.c4_input = None
        self.game_mode = 1
        self.input_valid = False
        self.c4_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}
        self.table = np.array([[0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]])

    # checking output if column is already full:
    @patch('builtins.print')
    def test_full_column(self, mock_print):
        self.c4_input = 'b'
        C4Game.validity_check(self)
        mock_print.assert_called_with("Column already full, pick another")

    # checking output if player entered an invalid column letter:
    @patch('builtins.print')
    def test_wrong_column(self, mock_print):
        self.c4_input = 'p'
        C4Game.validity_check(self)
        mock_print.assert_called_with("No such column, input must be a, b, c, d, e, f or g; or x to end game")

    # checking if variable will have the right value if the input is valid:
    def test_valid_input(self):
        self.c4_input = 'c'
        C4Game.validity_check(self)
        self.assertTrue(self.input_valid)


if __name__ == '__main__':
    unittest.main()
