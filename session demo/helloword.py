def print_board(board, n):
    for i in range(n):
        row = ""
        for j in range(n):
            if board[i] == j:
                row += "Q "
            else:
                row += ". "
        print(row)
    print("\n")

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_board(board, n)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(board, row + 1, n)

if __name__ == "__main__":
    n = int(input("Enter the value of N (e.g. 4, 5, 8): "))
    board = [-1] * n
    solve_n_queens(board, 0, n)