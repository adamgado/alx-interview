#!/usr/bin/python3
""" solves the N queens problem"""
import sys


def solution_search(r, n, cols, position, neg, board):
    """recurring function for nqueens"""
    if r == n:
        result = []
        for a in range(len(board)):
            for b in range(len(board[a])):
                if board[a][b] == 1:
                    result.append([a, b])
        print(result)
        return
    for x in range(n):
        if x in cols or (r + x) in position or (r - x) in neg:
            continue
        cols.add(x)
        position.add(r + x)
        neg.add(r - x)
        board[r][x] = 1
        solution_search(r+1, n, cols, position, neg, board)
        cols.remove(x)
        position.remove(r + x)
        neg.remove(r - x)
        board[r][x] = 0


def nqueens(n):
    """solves the N queens problem"""
    cols = set()
    position = set()
    neg = set()
    board = [[0] * n for a in range(n)]
    solution_search(0, n, cols, position, neg, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
