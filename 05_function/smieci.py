import numpy as np



# x = input("\n Player X choose: ")
#
# player_X(x)
#
# y = input("\n Player Y choose: ")
# player_Y(y)
#
# continue
board = [
     [" ",1 ,2 ,3],
    ["A",".",".","."],
    ["B",".",".","."],
    ["C",".",".","."],

]
def cheack_win(board):
    for row in board:


        if len(set(row)) == 1:
            print('Wygrywający to:', set(row))
            break
        else:
            continue

    board_transposed = np.transpose(board)
    for row2 in board:
        if len(set(row2)) == 1:
            print("Wygrywający to: ",set(row2))
            break
        else:
            continue

    for x in board:
        if [board[0,0] == board[1,1] == board[2,2]] or [board[0,2] == board[1,1] == board[2,0]]:
            print("Wygranym jest: ", x)
        else:
            continue
