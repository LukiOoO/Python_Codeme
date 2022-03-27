import numpy as np


def print_board(board):
    for i in board:
        print(" ")
        for x in i:
            print(x, end=" | ")


def player(x, symbol):
    if x == "A1":
        board[1][1] = symbol
        print_board(board)
    if x == "A2":
        board[1][2] = symbol
        print_board(board)
    if x == "A3":
        board[1][3] = symbol
        print_board(board)
    if x == "B1":
        board[2][1] = symbol
        print_board(board)
    if x == "B2":
        board[2][2] = symbol
        print_board(board)
    if x == "B3":
        board[2][3] = symbol
        print_board(board)
    if x == "C1":
        board[3][1] = symbol
        print_board(board)
    if x == "C2":
        board[3][2] = symbol
        print_board(board)
    if x == "C3":
        board[3][3] = symbol
        print_board(board)
    return board


def get_uniq_values(row):
    row_set = set(row)
    result = row_set - {"A", "B", "C", "1", "2", "3"}
    return result


def check_winer_line(table2D):
    print(table2D)
    for i in table2D:
        prepared_set = get_uniq_values(i)
        if len(prepared_set) == 1 and list(prepared_set)[0] in ['X', 'O']:
            print("\nWygrywający to:", prepared_set)


def check_win(board):
    # horizontal
    check_winer_line(board)

    # vertical
    board_transposed = np.transpose(board)
    check_winer_line(board_transposed)

    # diagonal
    for x in board:
        if (board[1][1] == board[2][2] == board[3][3]) or (board[1][3] == board[2][2] == board[3][1]):
            print("Wygranym jest: ", x)


print("Tic tac toe game ")
print("-------------------------------------------------------")

board = [
    [" ", 1, 2, 3],
    ["A", ".", ".", "."],
    ["B", ".", ".", "."],
    ["C", ".", ".", "."],
]
print_board(board)

move_counter = 0

while move_counter < 3:
    o = input("\n Player O choose: ")
    player(o, 'O')

    x = input("\n Player X choose: ")

    player(x, "X")
    move_counter += 1

check_win(board)
