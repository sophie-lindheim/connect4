import numpy as np


def c4_implement_move():
    c4_input = 'b'
    game_mode = 1
    actual_player = 2
    input_valid = False
    c4_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}
    table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]])
    headers = ['a b c d e f g']

    # temp variable for index of column number

    i = c4_dict[c4_input]

    # checking from bottom up the elements of the selected column

    if table[5][i] == 0:
        table[5][i] = actual_player
    elif table[4][i] == 0:
        table[4][i] = actual_player
    elif table[3][i] == 0:
        table[3][i] = actual_player
    elif table[2][i] == 0:
        table[2][i] = actual_player
    elif table[1][i] == 0:
        table[1][i] = actual_player
    elif table[0][i] == 0:
        table[0][i] = actual_player

    # Resetting input:

    c4_input = None

    print(table)
    print(c4_input)


if __name__ == '__main__':
    c4_implement_move()