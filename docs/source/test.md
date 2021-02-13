# Test descriptions
## The tested functions
The functions which take input or implement something in a table are using python basic functionality, so although
it would be possible to test them, we didn't find a lot of value in that. It was also specified in the assignment 
description, that we don't have to test the game play functionality.For this reason we decided to test 
the 2 main decision-making functions of the game: validity check function and check winner function.

1. validity check function test: we check 3 cases: the first method tests if the function reacts correctly if an 
   input comes to an already full column. The second method tests, if the function reacts correctly if
   the input is not a valid column letter. The third tests is the function changes the right variable to 
   the right value with a valid input. With this we have 100% test coverage.
   
   
2. check winner function test: Four different win cases are tested; winning by putting four stones in a column, in a 
   row and each options in a diagonal. Each of these winning case will also be checked for each player options;
   one, two and the computer. The first four methods tests if the game terminates with end_game variable value 
   True after every player has won by putting four stones in a row. The second stack of four methods tests if
   the game terminates with end_game variable value True after every player has won by putting four stones 
   in a column. The third and fourth stack of four methods tests if every player has won by putting four 
   stones in each way of a diagonal. All in all there 12 tests to pass. In this function we also reached 100% 
   test coverage by this.


