import random

def player_input(board, currentPlayer):
    while True:
            inp = int(input("Enter a number 1-9: "))
            if 1 <= inp <= 9 and board[inp - 1] == ' ':
                board[inp - 1] = currentPlayer
                break
            elif 1 <= inp <= 9:
                print('Field is already taken')
            else:
                print('Invalid number')

def computer_move(board):
    empty_cells = [i for i, cell in enumerate(board) if cell == " "]
    if empty_cells:
        move = random.choice(empty_cells)
        board[move] = "O"