import random
import time


ROWS = 30
COLS = 60


board = [[random.randint(0, 1) for j in range(COLS)] for i in range(ROWS)]


def display_board(board):
    for row in board:
        for col in row:
            if col == 1:
                print("#", end="")
            else:
                print(".", end="")
        print()

def count_neighbors(board, row, col):
    count = 0
    for i in range(max(0, row-1), min(row+2, ROWS)):
        for j in range(max(0, col-1), min(col+2, COLS)):
            if (i, j) != (row, col) and board[i][j] == 1:
                count += 1
    return count


def update_board(board):
    new_board = [[0 for j in range(COLS)] for i in range(ROWS)]
    for i in range(ROWS):
        for j in range(COLS):
            neighbors = count_neighbors(board, i, j)
            if board[i][j] == 1:
                if neighbors in [2, 3]:
                    new_board[i][j] = 1
            else:
                if neighbors == 3:
                    new_board[i][j] = 1
    return new_board


while True:
    display_board(board)
    board = update_board(board)
    time.sleep(0.5)
