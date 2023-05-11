# Tic-Tac-Toe-Game-Tree
Calculates and displays an evaluation of a tictactoe game tree

Consider the game Tic-Tac-Toe. Let Xn be the number of rows, columns or diagonals with exactly n X's and no Os. Similarly On is the number of rows, columns, or diagonals with n Os and no Xs. The utility functions assign +1 to any position with X3 = 1 and -1 to any position with O3 = 1. All other terminal positions have utility 0. For non-terminal positions, we use a linear evaluation function defined as Eval(s) = 3X2(s) +X1(s)-(3O2(s)+O1(s)).

a. Approximately how many possible games of Tic-Tac-Toe are there?

There are 255168 possible games of tic tac toe excluding symmetry. With symmetry it’s 9!=9*8*7*6*5*4*3*2*1 which is 362,880.


b. Show the whole game tree starting from an empty board down to depth 2 (i.e., one X and one O on the board), taking symmetry into account.

Empty    →	First Move  →	Option1   OR	Option2    OR	Option3
[- - -]		[ X - -]		[X  O -]		[X -  -]		[X -  -]
[- - -]		[ - - -]		[-  - -]		[O -  -]		[- O  -]
[- - -]		[ - - -]		[-  - -]		[- -  -]		[- -  -]

[- - -]		[ - X -]		[O X -]		   [- X O]		[- X  -]
[- - -]		[ - -  -]		[-  -  -]		[- -   -]		[- O  -]
[- - -]		[ - -  -]		[-  -  -]		[- -   -]		[- -   -]
									OR	Option 4
[- - -]		[ - - -]		[O  - -]		[- -  -]		[- -  -]		[- -  -]
[- - -]		[ - X -]		[-  X -]		[O X  -]		[- X  O]		[- X  -]
[- - -]		[ - - -]		[-  -  -]		[- -  -]		[- -  -]		[O -  -]

c. Mark on your tree the evaluations of all positions at depth 2.

THis is where the script comes in. The evaluation function isn't suitable for depth 2, as all of the evaluations result in 0.

### Script output
X O -
- - -
- - -

X2: 1
O2: 1
Calculation: 3*1 + 1 - (3*1 + 1) = 0
Evaluation: 0

X - -
O - -
- - -

X2: 1
O2: 1
Calculation: 3*1 + 1 - (3*1 + 1) = 0
Evaluation: 0

X - -
- O -
- - -

X2: 1
O2: 1
Calculation: 3*1 + 1 - (3*1 + 1) = 0
Evaluation: 0

X - -
- - O
- - -

X2: 1
O2: 1
Calculation: 3*1 + 1 - (3*1 + 1) = 0
Evaluation: 0

X - -
- - -
- O -

X2: 1
O2: 1
Calculation: 3*1 + 1 - (3*1 + 1) = 0
Evaluation: 0

X - -
- - -
- - O

X2: 1
O2: 1
Calculation: 3*1 + 1 - (3*1 + 1) = 0
Evaluation: 0

- X -
O - -
- - -

X2: 1
O2: 1
Calculation: 3*1 + 1 - (3*1 + 1) = 0
Evaluation: 0

- X -
- O -
- - -

X2: 1
O2: 1
Calculation: 3*1 + 1 - (3*1 + 1) = 0
Evaluation: 0

- X -
- - O
- - -

X2: 1
O2: 1
Calculation: 3*1 + 1 - (3*1 + 1) = 0
Evaluation: 0

- X -
- - -
- O -

X2: 1
O2: 1
Calculation: 3*1 + 1 - (3*1 + 1) = 0
Evaluation: 0

- X -
- - -
- - O

X2: 1
O2: 1
Calculation: 3*1 + 1 - (3*1 + 1) = 0
Evaluation: 0

- O -
- X -
- - -

X2: 1
O2: 1
Calculation: 3*1 + 1 - (3*1 + 1) = 0
Evaluation: 0

- - -
O X -
- - -

X2: 1
O2: 1
Calculation: 3*1 + 1 - (3*1 + 1) = 0
Evaluation: 0

- - -
- X O
- - -

X2: 1
O2: 1
Calculation: 3*1 + 1 - (3*1 + 1) = 0
Evaluation: 0

- - -
- X -
- O -

X2: 1
O2: 1
Calculation: 3*1 + 1 - (3*1 + 1) = 0
Evaluation: 0

- - -
- X -
- - O

X2: 1
O2: 1
Calculation: 3*1 + 1 - (3*1 + 1) = 0
Evaluation: 0




