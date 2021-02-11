import random
import numpy as np


class C4Game:
    """The class containing our Connect 4 game modules.

    In this class there are 5 methods, one main called connect4, which should be called to run the game.
    connect4_input asks for player input, validity_check does what is in it's name for each move,
    check_winner does also what it is called, after each move. If these both are passed, c4_implement_move
    implements the move on the table.

    """

    def __init__(self):
        """__init__ method of the C4Game class, initializing attributes.

        This method doesn't work with parameters, just initializes the attributes for the game.
        They are described below.

        """

        #: dict of str: int: Dictionary to identify columns of the game table.
        self.c4_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}

        #: list of str: List to printout as the row headers.
        self.headers = ['a b c d e f g']

        #: numpy array: Lists of integers. The game table.
        self.table = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

        #: bool: attribute to contain information if the game has been terminated.
        self.end_game = False

        #: int: 1 or 2, the number of the actual player.
        self.actual_player = 1

        #: str: variable to hold the game input from the actual player.
        self.c4_input = None

        #: int: 1 or 2, number of human players.
        self.game_mode = 1

        #: bool: attribute to contain information if the actual input is valid or not.
        self.input_valid = False

    def connect4(self):
        """Main function, that runs the connect 4 game.

        This function works with the attributes defined in the class. First it prints out the greeting and
        asks the player(s) to indicate if 1 person will play against the computer or 2 against each other.
        Then it prints out the game table and the rules. Next, it calls the connect4_input function, asking
        the first player for input. If the player input is to abort the game, this will be done and the game
        terminates. If not, the validity_check method will be called to check the actual input.
        Next the input will be implemented on the table by c4_implement_move method and the table will be
        printed out. Next the check_winner method will check the table, and if there is a winner, it will
        be announced and the game terminates. If not, the above cycle will be repeated, alternating between
        the players, as long as one terminates or wins the game.

        Returns
        -------
        None

        """

        print("Welcome to our little connect 4 game!\n")
        print("Please enter how many humans will play: 1 against the computer or 2 against each other:\n")

        ch_np = int(input())

        while not (ch_np == 1 or ch_np == 2):
            print("Please enter 1 or 2")
            ch_np = int(input())

        self.game_mode = ch_np

        print("In each round you will be asked to enter a letter between a to g, which stands for \n"
              "the column you want to put your stone in. Your stone will be shown as your player number\n"
              "in the table. Then the other player (AI or actual player, depends) does the same thing.\n"
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

        This function works with the variables defined in the class. To be used after each step, to check
        if the actual player who took this step is a winner. First the function defines the winning
        sequence based on the actual player's number. Then checks first the rows, then the columns, then the
        left-to-right diagonals, then the right-to-left diagonals, if the actual table contains the winning
        sequence. If the winner sequence is found, the end_game variable is set to True and the function terminates.

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

        This function works with the variables defined in the class. First it checks if the actual player is
        the computer. If yes, the c4_input will be generated as a random lowercase letter between a - g.
        If the actual_player is not the computer, the player will be asked for an input, which will be saved in the
        c4_input variable.

        Returns
        -------
        None

        """

        if self.game_mode == 1 and self.actual_player == 2:  # if actual player is computer, generates the input
            # as random
            letters = "abcdefg"
            self.c4_input = random.choice(letters)
        else:  # if actual player is not the computer, asks the actual player for input
            print("\nPlayer", self.actual_player, ": type column letter (between a-g) or x to end game,"
                                                  " then press enter")
            temp_variable = str(input())
            if temp_variable == 'x':
                self.end_game = True
            else:
                self.c4_input = temp_variable

    def validity_check(self):
        """Checks if the actual input is valid in the game.

        This function works with the variables defined in the class and with the input collected in the
        connect4_input function. First it checks if the actual value of the c4_input variable is a lowercase character
        in the range from a to g, as a column in the game. If not, a message will be displayed if the actual_player is
        not the computer, and the function will end with the input_valid variable as False.
        If the c4_input is a valid character, then the function will check if the column defined by c4_input is full.
        If yes, an error message will be displayed for human players and the function will end with the input_valid
        variable as False.
        If the input is valid, the function will set the input_valid variable to True.

        Returns
        -------
        None

        """

        if self.c4_input not in self.c4_dict:  # checks if current input is a - g
            print("No such column, input must be a, b, c, d, e, f or g; or x to end game")
        elif self.table[0, self.c4_dict[self.c4_input]] != 0:  # checks if the top row is not 0, meaning column
            # is already full
            if ((self.game_mode == 1) and (self.actual_player == 1)) or (
                    self.game_mode == 2):  # error message only if human player
                print("Column already full, pick another")
        else:
            self.input_valid = True

    def c4_implement_move(self):
        """Checks if the actual input is valid in the game.

        This function works with the variables defined in the class and with the input collected in the
        connect4_input function. It check the defined column of the game table from the lowest row upwards,
        if an element is zero. The first one it finds, exchanges it to the number of the actual player.
        Finally it resets the c4_input variable to None.

        Returns
        -------
        None

        """

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
