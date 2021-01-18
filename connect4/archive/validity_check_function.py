import numpy as np


def validity_check():
    """Checks if the actual input is valid in the game.

    This function works with the variables defined in the game function and with the input collected in the
    connect4_input function. First it checks if the actual value of the c4_input variable is a lowercase character
    in the range from a to g, as a column in the game. If not, a message will be displayed if the actual_player is
    not the computer, and the function will end with the input_valid variable as False.
    If the c4_input is a valid character, then the function will check if the column defined by c4_input is full.
    If yes, an error message will be displayed for human players and the function will end with the input_valid
    variable as False.
    If the input is valid, the function will set the input_valid variable to True.

    Parameters
    -----------
    this function uses parameters defined in the game_function

    Returns
    -------
    None

    """

    # variables in game globally defined by game function, need to be taken away for final version:
    c4_input = 'f'
    game_mode = 1
    actual_player = 2
    input_valid = False
    c4_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}
    table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    if c4_input not in c4_dict:  # checks if current input is a - g
        print("No such column, input must be a, b, c, d, e, f or g; or x to end game")
    elif table[0, c4_dict[c4_input]] != 0:  # checks if the top row is not 0, meaning column is already full
        if (game_mode == 1 and actual_player == 1) or (game_mode == 2):  # error message only if human player
            print("Column already full, pick another")
    else:
        input_valid = True
    return print(input_valid)  # needs to be taken away for final version


if __name__ == '__main__':
    validity_check()
