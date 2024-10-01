#!/usr/bin/python3
"""Returns list representing the Pascal's triangle"""


def pascal_triangle(n):
    """returns pascal's triangle"""
    plist = []
    if n <= 0:
        return plist
    for a in range(n):
        row = [1]
        if plist:
            last = plist[-1]
            row.extend([sum(x_y) for x_y in zip(last, last[1:])])
            row.append(1)
        plist.append(row)
    return (plist)
