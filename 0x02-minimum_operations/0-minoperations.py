#!/usr/bin/python3
"""calculate fewest number of operations to result in exactly n H characters"""


def minOperations(n):
    """Returns an integer number of operations"""
    op = 0
    min = 2
    while n > 1:
        while n % min == 0:
            op += min
            n /= min
        min += 1
    return op
