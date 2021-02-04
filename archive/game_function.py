import numpy as np
import random


def connect4():
    """ A little game of connect 4.
        This function works as game of connect 4. To be used the user enters an Input between 1-2.
        The function starts a game sequence where several things happen further described in the code with line
        comments. It checks if the actual player is the computer. If yes, the c4_input will be generated as a random
        lowercase letter between a - g. If the actual_player is not the computer, the player will be asked for an input,
        which will be saved in the c4_input variable.To check if the actual player who took this step is a winner
        sequence based on the actual player's number. Then checks first the rows, then the columns, then the
        left-to-right diagonals, then the right-to-left diagonals, if the actual table contains the winning sequence.
        If the winner sequence is found, the end_game variable is set to True and the function terminates.

        Parameters
        -----------

        Returns
        -------
        None

        """
    end_game = False
    actual_player = 0
    c4_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}
    table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])
    while end_game is False:
        print("Welcome to our little connect 4 game!\n"
              "First you will select whether you want to play against an AI or against each other.\n"
              "After that you will be asked to enter a letter between a to g, which stands for \nthe row you want to"
              "put your stone in. Then the other player (AI or actual player, depends)\ndoes the same thing. "
              "The winner is the player with four stones in a row, column or diagonal.\nIf you are unsure, "
              "the game will tell you if you, the other player or the AI has won.")
        print(table)
        print("Please enter 1 if you want to play against an AI or 2 if you want "
              "to play against each other:")
        game_mode = input("Please enter 1 if you want to play against an AI or 2 if you want to play against each"
                          "other:")
        if game_mode == 1:
            actual_player += 1
        else:
            actual_player += 2
        input_valid = False
        while input_valid is False:
            while game_mode == 1 and actual_player == 2:
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
        if c4_input not in c4_dict:  # checks if current input is a - g
            print("No such column, input must be a, b, c, d, e, f or g; or x to end game")
        elif table[0, c4_dict[c4_input]] != 0:  # checks if the top row is not 0 -> column is already full
            if (game_mode == 1 and actual_player == 1) or (game_mode == 2):  # error message only if human player
                print("Column already full, pick another")
            else:
                input_valid = True
    if c4_input == 'a':
        if table[6, 0] == 0:
            table[6, 0] = actual_player
        else:
            table[5, 0] = actual_player
    elif c4_input == 'b':
        table[6, 1] = actual_player
        actual_player += 1
        print(table)


if __name__ == '__main__':
    connect4()
