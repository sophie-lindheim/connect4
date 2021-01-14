import random

import numpy as np


def play(n=None):
    """ A little game of connect 4 which will be started with this function.
        This function works as game of connect 4. To be used the user enters an Input between 1-2 to choose, whether
        he/she wants to play against an KI [1] or against another player [2].
        The function starts a game sequence where several things happen further described in the code.
        First, it will expect the user to enter a letter between a-g to choose a row to put his/her stone into.


        Parameters
        -----------
        n
            Works as boolean to keep the game running while the user/s play a round of connect 4.

        Returns
        -------
        c4_input
            Parameter for further functions to validity & implement the input/move on the board.

        """
    if n is None:
        while True:
            try:
                n = int(input("Welcome to our little connect 4 game!\n"
                              "First you will select whether you want to play against an AI or against each other.\n"
                              "After that you will be asked to enter a letter between a to g, which stands for \nthe"
                              " row you want to put your stone in. Then the other player (AI or actual player, depends)"
                              "\ndoes the same thing. The winner is the player with four stones in a row, column or"
                              " diagonal.\nIf you are unsure, the game will tell you if you, the other player or"
                              "the AI has won."))
            except ValueError:
                print('Invalid input')
                continue
            if n <= 0:
                print('Invalid input')
                continue
            break
    game_mode = n
    c4_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}
    table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])
    print(table)
    actual_player = 1
    while True:
        c4_input = get_input(actual_player, table, game_mode)
        implement_move_on_table(c4_input, actual_player, table)
        print(table)

        if check_winner(table, actual_player) or check_winner(zip(*table), actual_player):
            print('Player', actual_player, 'has won')
        return c4_input


def get_input(actual_player, c4_input, game_mode, end_game=False):
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
        return c4_input


def check_column_emptiness(table) -> bool:
    for each in table:
        pass
    return True


def implement_move_on_table(c4_input, actual_player, table):
    """Implements the input (c4_input) onto the game table.

        This function works with the variables given to it by the play() function and the get_input().
        It put's the stone where the user or KI wanted it to put in. Afterwards it displays the new table.

        Parameters
        -----------
        c4_input
            The input given by the user in get_input()
        actual_player
            The player who may be the winner / is currently at his/her turn
        table
            The displayed table of the connect 4 game

        Returns
        -------
        Nothing yet, but the return should be the new table.

        """

    for each in table:
        if each.c4_input == 'a':
            if table[6, 0] == 0:
                table[6, 0] = actual_player
            else:
                table[5, 0] = actual_player
        elif each.c4_input == 'b':
            table[6, 1] = actual_player
            actual_player += 1
            print(table)


def check_winner(actual_player, table):
    """Checks the actual game table if there is a winner.

        This function works with the variables given to it by the play() function. To be used after each step, to check
        if the actual player who took this step is a winner. First the function defines the winning
        sequence based on the actual player's number. Then checks first the rows, then the columns, then the
        left-to-right diagonals, then the right-to-left diagonals, if the actual table contains the winning sequence.
        If the winner sequence is found, the end_game variable is set to True and the function terminates.

        Parameters
        -----------
        actual_player
            The player who may be the winner / is currently at his/her turn
        table
            The displayed table of the connect 4 game

        Returns
        -------
        None

        """

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
    play()
