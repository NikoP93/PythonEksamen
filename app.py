from board import print_board, create_board
from input_handler import player_input,computer_move
from win_checker import check_win_conditions
from history import save_history

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

        if move_count >= 5 and (check_win_conditions(board) or move_count == 9):
            print_board(board)
            print(f"{current_player} wins!" if check_win_conditions(board) else "It's a draw!")
            
            text = f'{("Player" if current_player == "X" else "Computer")} won in {move_count} moves' \
                    if check_win_conditions(board) else f"It's a draw in {move_count} moves"

            save_history(text)
            break

        # Swap player
        current_player = "O" if current_player == "X" else "X"
        
    # Play again option
    should_continue = input("Play again? (y/n): ").lower()
    if should_continue == "y":
        play_game()

play_game()
       