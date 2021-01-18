import random
import numpy as np


class C4Game:
    def __init__(self):
        self.c4_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}
        self.headers = ['a b c d e f g']
        self.table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])
        self.end_game = False
        self.actual_player = 1
        self.c4_input = None
        self.game_mode = 1
        self.input_valid = False

    def connect4(self):
        print("Welcome to our little connect 4 game!\n")
        print("Please enter how many humans will play: 1 against the computer or 2 against each other:\n")

        ch_np = int(input())

        while not (ch_np == 1 or ch_np == 2):
            print("Please enter 1 or 2")
            ch_np = int(input())

        self.game_mode = ch_np

        print("In each round you will be asked to enter a letter between a to g, which stands for \n"
              "the column you want to put your stone in. Your stone will be shown as your player number in the table\n"
              "Then the other player (AI or actual player, depends)does the same thing.\n"
              "The winner is the player with four stones in a row, column or diagonal.\n"
              "Here is your game board:\n")

        print(self.headers)
        print(self.table)

        while not self.end_game:
            while not (self.input_valid or self.end_game):
                self.connect4_input()
                if not self.end_game:
                    self.validity_check()

            if not self.end_game:
                self.c4_implement_move()
                # print out a message if computer moves:
                if self.game_mode == 1 and self.actual_player == 2:
                    print(f'\nThe computer moves:')
                print(self.headers)
                print(self.table)
                self.check_winner()
                if self.end_game:
                    print(f'\nPlayer {self.actual_player} has won!')
                    return
                else:
                    if self.actual_player == 1:
                        self.actual_player = 2
                    else:
                        self.actual_player = 1
                    self.input_valid = False
            else:
                print(f'Player {self.actual_player} has ended the game.')
                return

    def check_winner(self):
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

        # local variable, to define winning sequence
        w_s = ""

        if self.actual_player == 1:
            w_s = "1 1 1 1"
        elif self.actual_player == 2:
            w_s = "2 2 2 2"

        # checking winner sequence in rows:
        for row in self.table:
            if w_s in str(row):
                self.end_game = True
                return

        # checking winner sequence in columns:
        for col in self.table.T:
            if w_s in str(col):
                self.end_game = True
                return

        # checking winner sequence in normal diagonals:
        for index in range(-2, 4):
            diag = self.table.diagonal(index)
            if w_s in str(diag):
                self.end_game = True
                return

        # flipping array and checking winner sequence in backward diagonals:
        flipped = np.fliplr(self.table)
        for index in range(-2, 4):
            diag = flipped.diagonal(index)
            if w_s in str(diag):
                self.end_game = True
                return

    def connect4_input(self):
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

        if self.game_mode == 1 and self.actual_player == 2:  # if actual player is computer, generates the input as random
            letters = "abcdefg"
            self.c4_input = random.choice(letters)
        else:  # if actual player is not the computer, asks the actual player for input
            print("\nPlayer", self.actual_player, ": type column letter (between a-g) or x to end game, then press enter")
            temp_variable = str(input())
            if temp_variable == 'x':
                self.end_game = True
            else:
                self.c4_input = temp_variable

    def validity_check(self):
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

        if self.c4_input not in self.c4_dict:  # checks if current input is a - g
            print("No such column, input must be a, b, c, d, e, f or g; or x to end game")
        elif self.table[0, self.c4_dict[self.c4_input]] != 0:  # checks if the top row is not 0, meaning column is already full
            if ((self.game_mode == 1) and (self.actual_player == 1)) or (self.game_mode == 2):  # error message only if human player
                print("Column already full, pick another")
        else:
            self.input_valid = True

    def c4_implement_move(self):
        # temp variable for index of column number
        i = self.c4_dict[self.c4_input]

        # checking from bottom up the elements of the selected column
        if self.table[5][i] == 0:
            self.table[5][i] = self.actual_player
        elif self.table[4][i] == 0:
            self.table[4][i] = self.actual_player
        elif self.table[3][i] == 0:
            self.table[3][i] = self.actual_player
        elif self.table[2][i] == 0:
            self.table[2][i] = self.actual_player
        elif self.table[1][i] == 0:
            self.table[1][i] = self.actual_player
        elif self.table[0][i] == 0:
            self.table[0][i] = self.actual_player

        # Resetting input:
        self.c4_input = None


if __name__ == '__main__':
    g = C4Game()
    g.connect4()

