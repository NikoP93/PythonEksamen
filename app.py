from board import print_board, create_board
from input_handler import player_input,computer_move
from win_checker import check_win_conditions

def play_game():
    board = create_board()
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
       