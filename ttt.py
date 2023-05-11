# Tic Tac Toe game board is represented as a list of lists
# 'X' represents X player, 'O' represents O player, and '-' represents an empty square

import numpy as np

def empty_board():
    return [['-' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def eval_position(board):
    X2 = len([1 for i in range(3) for j in range(3) if board[i][j] == 'X'])
    O2 = len([1 for i in range(3) for j in range(3) if board[i][j] == 'O'])
    print('X2:', X2)
    print('O2:', O2)
    print('Calculation: 3*{} + {} - (3*{} + {}) = {}'.format(X2, X2, O2, O2, 3*X2 + X2 - (3*O2 + O2)))
    return 3*X2 + X2 - (3*O2 + O2)

first_moves = [(0, 0), (0, 1), (1, 1)]  # corner, edge, center
second_moves = [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1), (2, 2)]  # all possible second moves, considering symmetry

for first in first_moves:
    for second in second_moves:
        # don't place O on top of X
        if second == first:
            continue
        board = empty_board()
        board[first[0]][first[1]] = 'X'
        board[second[0]][second[1]] = 'O'
        print_board(board)
        print('Evaluation:', eval_position(board))
        print()
