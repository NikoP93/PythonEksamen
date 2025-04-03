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