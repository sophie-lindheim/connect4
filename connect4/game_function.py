import numpy as np
import random
from typing import Dict


def connect4():
    """ A little game of connect 4.
    """
    game_mode = 0
    end_game = False
    input_valid = None
    actual_player = 0
    c4_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}
    table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])
    while end_game is False:
        print("Welcome to our little connect 4 game! First you will select whether you want to play against an AI or"
              "against each other. After that")
        print(table)
        print("Please enter 1 if you want to play against an AI or 2 if you want"
              "to play against each other:")
        game_mode = int(input())
        actual_player = 2
        while input_valid is False or end_game is False:
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
                if end_game is False:
                    if c4_input not in c4_dict:  # checks if current input is a - g
                        print("No such column, input must be a, b, c, d, e, f or g; or x to end game")
                    elif table[0, c4_dict[c4_input]] != 0:  # checks if the top row is not 0 -> column is already full
                        if (game_mode == 1 and actual_player == 1) or (
                                game_mode == 2):  # error message only if human player
                            print("Column already full, pick another")
                    else:
                        input_valid = True
        if end_game is False:
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