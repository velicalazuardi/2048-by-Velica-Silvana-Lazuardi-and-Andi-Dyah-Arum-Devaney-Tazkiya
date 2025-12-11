import random
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def create_board():
    board = [[0]*4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty = [(i,j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty:
        i,j = random.choice(empty)
        board[i][j] = 2 if random.random() < 0.9 else 4

def print_board(board):
    clear()
    print("===== 2048 GAME =====")
    for row in board:
        print("+------"*4 + "+")
        print("".join(f"|{str(num).center(6) if num!=0 else '      '}" for num in row) + "|")
    print("+------"*4 + "+")
    print("\nW A S D untuk gerak. Q untuk keluar ges.\n")

def compress(row):
    new_row = [i for i in row if i != 0]
    new_row += [0] * (4 - len(new_row))
    return new_row

def merge(row):
    for i in range(3):
        if row[i] != 0 and row[i] == row[i+1]:
            row[i] *= 2
            row[i+1] = 0
    return row

def move_left(board):
    new_board = []
    for row in board:
        new_row = compress(row)
        new_row = merge(new_row)
        new_row = compress(new_row)
        new_board.append(new_row)
    return new_board

def move_right(board):
    new_board = []
    for row in board:
        new_row = row[::-1]
        new_row = compress(new_row)
        new_row = merge(new_row)
        new_row = compress(new_row)
        new_board.append(new_row[::-1])
    return new_board

def move_up(board):
    rotated = list(map(list, zip(*board)))
    moved = move_left(rotated)
    return [list(row) for row in zip(*moved)]

def move_down(board):
    rotated = list(map(list, zip(*board)))
    moved = move_right(rotated)
    return [list(row) for row in zip(*moved)]

def board_changed(old, new):
    return old != new

def game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if i < 3 and board[i][j] == board[i+1][j]:
                return False
            if j < 3 and board[i][j] == board[i][j+1]:
                return False
    return True

def main():
    board = create_board()
    
    while True:
        print_board(board)
        
        move = input("Gerak (W/A/S/D): ").lower()
        
        if move == "q":
            print("Yahh! Kamu kalah AWKWOAKW.")
            break
        
        if move not in ("w", "a", "s", "d"):
            continue
        
        old_board = [row[:] for row in board]
        
        if move == "w":
            board = move_up(board)
        elif move == "s":
            board = move_down(board)
        elif move == "a":
            board = move_left(board)
        elif move == "d":
            board = move_right(board)
        
        if board_changed(old_board, board):
            add_new_tile(board)
        
        if game_over(board):
            print_board(board)
            print("TETOTT! UDAH GABISA GERAKK.")
            break

if __name__ == "__main__":
    main()
