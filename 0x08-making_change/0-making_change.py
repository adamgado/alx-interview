#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """determine fewest coins needed to meet total"""
    if total <= 0:
        return 0
    sum = 0
    num = 0
    coins.sort(reverse=True)
    for a in coins:
        while sum < total:
            sum += a
            num += 1
        if sum == total:
            return num
        sum -= a
        num -= 1
    return -1
