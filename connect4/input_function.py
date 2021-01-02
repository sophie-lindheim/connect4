import random


def connect4_input():
    # variables in game globally defined by game function:
    c4_input = None
    game_mode = 2
    actual_player = 2
    end_game = False
    if game_mode == 1 and actual_player == 2:
        letters = "abcdefg"
        c4_input = random.choice(letters)
    else:
        print("Player", actual_player, ": type column letter (between a-g) or x to end game, then press enter")
        temp_variable = str(input())
        if temp_variable == 'x':
            end_game = True
        else:
            c4_input = temp_variable
    return f'{end_game}, {c4_input}'


if __name__ == '__main__':
    print(connect4_input())