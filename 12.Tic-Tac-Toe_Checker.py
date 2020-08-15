'''
If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we?
Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X",
or 2 if it is an "O", like so:

[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
We want our function to return:

-1 ==> if the board is not yet finished (there are empty spots),
1 ==> if "X" won,
2 ==> if "O" won,
0 ==> if it's a cat's game (i.e. a draw).

You may assume that the board passed in is valid in thecontext of a game of Tic-Tac-Toe.
'''

def isSolved(board):
    new_board = [[elem if elem != 2 else 4 for elem in row] for row in board]

    h_sum = [sum(row) for row in new_board]
    diag1_sum = [sum([new_board[i][i] for i in range(3)])]
    diag2_sum = [sum([new_board[i][-i+2] for i in range(3)])]
    new_board_T = list(map(list, zip(*new_board)))
    v_sum = [sum(row) for row in new_board_T]
    all_sums = h_sum + v_sum + diag1_sum + diag2_sum
    if 3 in all_sums:
        return 1
    elif 12 in all_sums:
        return 2
    elif 0 in new_board[0] or 0 in new_board[1] or 0 in new_board[2]:
        return -1
    else:
        return 0

print(isSolved([[0, 0, 1], [0, 1, 2], [2, 1, 0]]))
print(isSolved([[1, 1, 1], [0, 1, 2], [2, 0, 0]]))
print(isSolved([[0, 0, 1], [2, 2, 2], [2, 1, 0]]))
print(isSolved([[1, 0, 1], [0, 1, 2], [2, 1, 1]]))
print(isSolved([[0, 0, 2], [0, 1, 2], [2, 1, 2]]))
