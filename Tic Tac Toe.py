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

    while True:
        print_board(board)  # Print the current board state
        print(f"Player {current_player}'s turn. Select row and column (0, 1, 2):")
       
        # Get user input for the row and column
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue  # Continue to the next iteration if input is invalid


        # Check if the chosen position is valid
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid position. Please choose row and column between 0 and 2.")
            continue
        if board[row][col] != ' ':
            print("Position already taken. Please choose another.")
            continue  # Continue to next iteration if the position is taken


        # Place the player's symbol on the board
        board[row][col] = current_player


        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)  # Show the final board
            print(f"Player {winner} wins!")
            break  # End the game if there's a winner


        # Check for a draw
        if is_board_full(board):
            print_board(board)  # Show the final board
            print("It's a draw!")
            break  # End the game if the board is full


        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()  # Start the game
