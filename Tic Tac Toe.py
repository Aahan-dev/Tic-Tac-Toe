def print_board(board): # `print_board` function prints the current state of the Tic-Tac-Toe board.
    """Print the current state of the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))  # Print each row with '|' separating the cells
        print("-" * 9)  # Print a separator line

def check_winner(board): # `check_winner` function checks for a winner in the Tic-Tac-Toe board.
   
    # Check rows and columns for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]  # Return the winner if found
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]  # Return the winner if found

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None  # No winner found

def is_board_full(board): # `is_board_full` function checks if the Tic-Tac-Toe board is full.
    
    for row in board:# Iterate through each row in the board
        if ' ' in row:  # If there's an empty space, the board is not full
            return False
    return True  # No empty spaces, board is full

def main(): # `main` function is the entry point of the Tic-Tac-Toe game.
    
    # Initialize the game board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # Starting player

    