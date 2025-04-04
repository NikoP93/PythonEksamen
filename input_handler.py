import random
from win_checker import check_win_conditions

def player_input(board, currentPlayer):
    while True:
        try:
            inp = int(input("Enter a number 1-9: "))
            if 1 <= inp <= 9 and board[inp - 1] == ' ':
                board[inp - 1] = currentPlayer
                break
            elif 1 <= inp <= 9:
                print('Field is already taken')
        except ValueError:
            print('Invalid number, please use 1-9')

def computer_move(board):
    # 1. Check if computer can win in next move
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_win_conditions(board):
                return
            board[i] = " "  # undo

    # 2. Block if player is about to win
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_win_conditions(board):
                board[i] = "O"
                return
            board[i] = " "  # undo

    # 3. Otherwise pick random
    empty_cells = [i for i, cell in enumerate(board) if cell == " "]
    if empty_cells:
        move = random.choice(empty_cells)
        board[move] = "O"
