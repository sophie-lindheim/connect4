import random

import numpy as np


def play(n=None):
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
        return


def get_input(actual_player, c4_input, game_mode, end_game=False):
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


def implement_move_on_table(c4_input, actual_player, table):
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
