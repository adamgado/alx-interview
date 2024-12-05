#!/usr/bin/python3
"""function that finds the perimeter of an island"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0
    perimeter = 0

    for a in range(height):
        for b in range(width):
            if grid[a][b] == 1:
                size += 1
                if (b > 0 and grid[a][b - 1] == 1):
                    edges += 1
                if (a > 0 and grid[a - 1][b] == 1):
                    edges += 1
        perimeter = size * 4 - edges * 2
    return perimeter
