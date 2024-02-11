import random

# Function to create the game board
def create_board():
    board = []
    for _ in range(5):
        board.append(["O"] * 5)
    return board

# Function to print the game board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Function to place ships randomly on the board
def place_ships(board):
    for _ in range(3):
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        board[row][col] = "X"

# Function to check if the guess hits a ship
def check_hit(board, guess_row, guess_col):
    if board[guess_row][guess_col] == "X":
        print("Congratulations! You hit a ship!")
        board[guess_row][guess_col] = "*"
    else:
        print("Oops! You missed the ship!")
        board[guess_row][guess_col] = "!"

# Main function of the game
def main():
    print("Welcome to the Battleship game!")
    print("Try to sink three ships!")
    print()
    board = create_board()
    place_ships(board)
    # For debugging: Uncomment the line below to see the ship placements
    # print_board(board)
    print()
    print_board(board)
    print()
    for turn in range(10):
        print(f"Turn {turn + 1}")
        guess_row = int(input("Enter row number (0 to 4): "))
        guess_col = int(input("Enter column number (0 to 4): "))
        if guess_row < 0 or guess_row > 4 or guess_col < 0 or guess_col > 4:
            print("Invalid input! Please enter valid row and column numbers.")
            continue
        check_hit(board, guess_row, guess_col)
        print_board(board)
        print

