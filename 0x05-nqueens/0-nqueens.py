#!/usr/bin/python3
import sys


solutions = []
n = 0
pos = None


def get_input():
    """Validates input and retrieves the board size."""
    global n
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
    return n


def is_attacking(pos0, pos1):
    """Checks if two queens are attacking each other."""
    # Same row, column, or diagonal
    return pos0[0] == pos1[0] or pos0[1] == pos1[1] or \
        abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def group_exists(group):
    """Checks if a solution already exists in solutions."""
    global solutions
    for solution in solutions:
        if sorted(solution) == sorted(group):
            return True
    return False


def build_solution(row, group):
    """Recursively builds solutions for placing queens."""
    global solutions, n
    if row == n:
        if not group_exists(group):
            solutions.append(group.copy())
        return
    for col in range(n):
        current_pos = (row, col)
        if all(not is_attacking(current_pos, queen_pos)
                for queen_pos in group):
            group.append(current_pos)
            build_solution(row + 1, group)
            group.pop()  # Backtrack


def get_solutions():
    """Initializes positions and starts building solutions."""
    global pos, n
    pos = [(i // n, i % n) for i in range(n * n)]  # Generate board positions
    build_solution(0, [])


n = get_input()
get_solutions()
for solution in solutions:
    print(solution)
