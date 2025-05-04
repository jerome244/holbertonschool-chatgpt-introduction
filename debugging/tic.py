def print_board(board):
    # Prints the game board.
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Checks if there is a winner.
    # Horizontally
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vertically
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]  # Initialize the 3x3 board
    player = "X"  # Starting player
    move_count = 0  # Track the number of moves made

    while not check_winner(board) and move_count < 9:
        print_board(board)
        
        # Input validation for row and column
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                
                # Check if the input is within valid range
                if 0 <= row < 3 and 0 <= col < 3:
                    if board[row][col] == " ":
                        board[row][col] = player
                        break  # Valid move, break out of the loop
                    else:
                        print("That spot is already taken! Try again.")
                else:
                    print("Invalid row or column! Please enter a number between 0 and 2.")
            except ValueError:
                print("Invalid input! Please enter integers only.")

        move_count += 1

        # Check if the game has a winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Switch players
        player = "O" if player == "X" else "X"

    if move_count == 9 and not check_winner(board):
        # If all cells are filled and no winner, it's a draw
        print_board(board)
        print("It's a draw!")

# Start the game
tic_tac_toe()
