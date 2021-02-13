# Description of the code implementation for the C4 project
## 1. Strategy, planning and splitting tasks
We started by making a plan, listing the different parts and steps of the project and setting up a 
meeting structure. 

The first step in code writing was to define the mechanism and structure of the code and define the
core game mechanism.

Important decision point was, how to implement and manipulate a game table, that can be shown in a visually
consistent, easy to understand way. A needed key feature was to be able to easily work with the diagonals 
on the table. Considering multiple possibilities, we decided to use **numpy array**. 
The main reason is that it is very easy to implement inputs and check the winner combinations. 
It also looks good printed out, without spaces, commas or any other disturbing separators in the game table.

We have decided to implement different functions for the main functionality separately, because some parts are
needed multiple times during the gameplay, and this way they are flexible to call anytime needed. Although some
functions are only called once per round, it is still much more structured and easy to follow, test and debug, 
if the functionality is written separately, not directly in the game function. The important information
can be transferred between the functions in variables. 
The following functions were defined:
* game function: to run the gameplay
* input function: to get the actual input from the user
* validity check function: to check the actual input
* implement move: based on the actual, validated input
* check winner: after each move, to check if it was a winner move

After the structure and functionality was decided, the code draft was created, just in a text file. 
Then we split the above mentioned 5 functions between us, then we implemented them. After the parts were ready,
they were put together in a class to a functional game.

## 2. Description of the functions
1. game function: In the game function the complicated mechanism was to realize that the game can be ended by user
   input at each step and also by completing the game objective. We solved it by implementing bool 
   variables for each case and running 2 "while" loops in each round to check their value.
2. input function: In the game table we use 0 for an empty cell, 1 for the stones of player 1 and 2 for the
   stones of player 2. The columns are marked by the letters from a to g. This way the standing is easily 
   identifiable all the time. It is also quite easy to check the standings using the numpy array table. 
   If the actual player is a human player, in the input function he has to input the letter for the chosen
   column or x to terminate the game. If the actual player is the computer, the input function generates a 
   random column number, we didn't have time to implement an ai opponent. The input is saved in a variable 
   that is available for the following functions.
3. validity check function: This function has 2 main tasks: to check if the input is an existing column letter
and to check if that column is already full. If the input is invalid, human players are requested to give a 
   new input, computer player gives new input in the background, until it's input is valid.
4. implement move function: if the input is valid and there is no request to terminate the game, the input will
be implemented in the table.
5. check winner function: the function runs through all the different possibilities of winner combination each 
   time a move is implemented. It is very easy to do with the numpy array. It would be possible to run
   this only after a certain number of steps are made, or only for the non-zero cells, but a complete 
   check is very quick to run, so there was no need to complicate the code.