#Setup board
def print_board(board):
    for i in range(0,9,3):
        print(" " + " | ".join(board[i:i+3]))
        if i < 6:
            print("---+---+---")
    print()

def create_board():
    return [" " for _ in range(9)]