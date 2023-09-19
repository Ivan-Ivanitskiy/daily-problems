import argparse

def n_queens(n):
    def is_safe(x, y):
        return y not in used_columns and x - y not in used_diagonals and x + y not in used_antidiagonals

    if n <= 0:
        return []

    queens = [(0, 0)]
    used_columns = {0}
    used_diagonals = {0}
    used_antidiagonals = {0}

    for x in range(1, n):
        for y in range(n):
            if is_safe(x, y):
                queens.append((x, y))
                used_columns.add(y)
                used_diagonals.add(x - y)
                used_antidiagonals.add(x + y)
                break

    return queens

    
def print_board(coordinates, N):
    board = [['.' for _ in range(N)] for _ in range(N)]

    for x, y in coordinates:
        if 0 <= x < N and 0 <= y < N:
            board[y][x] = 'Q'
        else:
            print(f"Coordinate ({x}, {y}) is out of bounds, fam. Skipping.")
    
    for row in board:
        print(' '.join(row))


def main(N):
    queens = n_queens(N)
    print_board(queens, N)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Solve the N-Queens problem.')
    parser.add_argument('N', type=int, help='The size of the chess board and the number of queens.')

    args = parser.parse_args()
    
    main(args.N)

