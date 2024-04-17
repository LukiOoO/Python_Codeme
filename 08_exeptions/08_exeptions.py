# Pracuje nad udoskonaleniem tic tac toe game nie długo będzię

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
    #print(table2D)
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
            print("\nWygranym jest: ", x)





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
while move_counter < 7:
    user_list = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]

    while True:
        try:
            o = input("\n Player O choose: ")
            if o in user_list:
                player(o, 'O')
                move_counter += 1
                break
            else:
                raise ValueError

        except ValueError:
            print("Nie poprawna wartość podaj jeszcze raz")
            print_board(board)

    while True:
        try:
            x = input("\n Player X choose: ")

            if x in user_list:
                player(x, "X")
                move_counter += 1
                break
            else:
                raise ValueError

        except ValueError:
            print("Nie poprawna wartość podaj jeszcze raz")
            print_board(board)

check_win(board)

