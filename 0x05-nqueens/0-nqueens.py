#!/usr/bin/env python3
import sys

def is_valid(board, row, col):
    # Check if it's safe to place a queen at the given position
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n):
    def solve(board, row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                solve(board, row + 1)

    solutions = []
    board = [-1] * n
    solve(board, 0)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        print([[i, j] for i, j in enumerate(solution)])

if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions)
