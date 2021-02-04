import random


def connect4_input():
    """Generates the actual game input through the computer or player input.

    This function works with the variables defined in the game function. First it checks if the actual player is
    the computer. If yes, the c4_input will be generated as a random lowercase letter between a - g.
    If the actual_player is not the computer, the player will be asked for an input, which will be saved in the
    c4_input variable.

    Parameters
    -----------
    this function uses variables defined in the game_function

    Returns
    -------
    None

    """

    # variables in game globally defined by game function, have to be deleted in the final version:
    c4_input = None
    game_mode = 2
    actual_player = 2
    end_game = False

    if game_mode == 1 and actual_player == 2:  # if actual player is computer, generates the input as random
        letters = "abcdefg"
        c4_input = random.choice(letters)
    else:  # if actual player is not the computer, asks the actual player for input
        print("Player", actual_player, ": type column letter (between a-g) or x to end game, then press enter")
        temp_variable = str(input())
        if temp_variable == 'x':
            end_game = True
        else:
            c4_input = temp_variable
    return f'{end_game}, {c4_input}'  # only here for testing, has to be deleted in the final version


if __name__ == '__main__':
    print(connect4_input())
