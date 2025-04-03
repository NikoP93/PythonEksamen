import random

#Setup board
def print_board(board):
    for i in range(0,9,3):
        print(" " + " | ".join(board[i:i+3]))
        if i < 6:
            print("---+---+---")
    print()

#player input

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
        

def check_win_horizontal(board):
    return (
        board[0] == board[1] == board[2] != ' ' or
        board[3] == board[4] == board[5] != ' ' or 
        board[6] == board[7] == board[8] != ' ')

def check_diagonal_win(board):
       return (
        board[0] == board[4] == board[8] != ' ' or
        board[2] == board[4] == board[6] != ' ')

def check_vertical_win(board):
       return (
        board[0] == board[3] == board[6] != ' ' or
        board[1] == board[4] == board[7] != ' ' or 
        board[2] == board[5] == board[8] != ' ')


def check_win_conditions(board):
    return (
        check_win_horizontal(board) or
        check_diagonal_win(board) or
        check_vertical_win(board)
        )


def play_game():
    board = [" " for _ in range(9)]
    current_player = "X"
    move_count = 0
    playing = True

    while playing:
        print_board(board)

        if current_player == "X":
            player_input(board, current_player)
        else:
            computer_move(board)
            print("Computer made its move.")

        move_count += 1

        if move_count >= 5 and check_win_conditions(board):
            print_board(board)
            print(f"{current_player} wins!")
            break

        if move_count == 9:
            print_board(board)
            print("It's a draw!")
            break

        # Swap player
        current_player = "O" if current_player == "X" else "X"

    # Play again option
    should_continue = input("Play again? (y/n): ").lower()
    if should_continue == "y":
        play_game()

play_game()
       