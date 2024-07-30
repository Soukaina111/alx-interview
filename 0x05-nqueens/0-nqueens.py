#!/usr/bin/python3
"""
Solution to the nqueens problem
"""
import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    Backtrack function to find solution
    Args:
        r (int): Current row
        n (int): Number of queens
        cols (set): Set of occupied columns
        pos (set): Set of occupied positive diagonals
        neg (set): Set of occupied negative diagonals
        board (list): Representation of the board
    """
    if r == n:
        # Base case - all queens are placed
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return

    for c in range(n):
        if c in cols or (r + c) in pos or (r - c) in neg:
            # Current position is not safe, skip it
            continue

        # Mark the current position as occupied
        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        # Recursive call to place the next queen
        backtrack(r+1, n, cols, pos, neg, board)

        # Backtrack - remove the current position from the occupied sets
        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Solution to nqueens problem
    Args:
        n (int): Number of queens. Must be >= 4
    Return:
        List of lists representing coordinates of each
        queen for all possible solutions
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        # Incorrect usage, print the correct usage
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            # N must be at least 4
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        # N is not a number
        print("N must be a number")
        sys.exit(1)
