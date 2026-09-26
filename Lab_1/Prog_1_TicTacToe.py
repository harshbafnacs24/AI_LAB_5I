import random

board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def computer_move():

    empty_positions = []

    for i in range(9):
        if board[i] == " ":
            empty_positions.append(i)

    position = random.choice(empty_positions)

    board[position] = "O"

    print("Computer chose position", position + 1)


def game():

    for turn in range(9):

        print_board()

        print("Your turn (X)")

        position = int(input("Choose a position (1-9): ")) - 1

        if position < 0 or position > 8 or board[position] != " ":
            print("Invalid move! Try again.")
            continue

        board[position] = "X"

        if check_winner("X"):
            print_board()
            print("You win!")
            return

        if all(cell != " " for cell in board):
            print_board()
            print("It's a draw!")
            return


        computer_move()

        if check_winner("O"):
            print_board()
            print("Computer wins!")
            return

        
        if all(cell != " " for cell in board):
            print_board()
            print("It's a draw!")
            return


game()
