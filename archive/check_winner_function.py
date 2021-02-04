import numpy as np


def check_winner():
    """Checks the actual game table if there is a winner.

        This function works with the variables defined in the game function. To be used after each step, to check
        if the actual player who took this step is a winner. First the function defines the winning
        sequence based on the actual player's number. Then checks first the rows, then the columns, then the
        left-to-right diagonals, then the right-to-left diagonals, if the actual table contains the winning sequence.
        If the winner sequence is found, the end_game variable is set to True and the function terminates.

        Parameters
        -----------
        this function uses variables defined in the game_function

        Returns
        -------
        None

        """

    # variables in game globally defined by game function, need to be taken away for final version:
    end_game = False
    actual_player = 2
    table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    # local variable, to define winning sequence
    w_s = ""

    if actual_player == 1:
        w_s = "1 1 1 1"
    elif actual_player == 2:
        w_s = "2 2 2 2"

    # checking winner sequence in rows:
    for row in table:
        if w_s in str(row):
            end_game = True
            return

    # checking winner sequence in columns:
    for col in table.T:
        if w_s in str(col):
            end_game = True
            return

    # checking winner sequence in normal diagonals:
    for index in range(-2, 4):
        diag = table.diagonal(index)
        if w_s in str(diag):
            end_game = True
            return

    # flipping array and checking winner sequence in backward diagonals:
    flipped = np.fliplr(table)
    for index in range(-2, 4):
        diag = flipped.diagonal(index)
        if w_s in str(diag):
            end_game = True
            return


if __name__ == '__main__':
    check_winner()
