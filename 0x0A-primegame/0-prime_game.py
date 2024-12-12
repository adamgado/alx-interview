#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """determine who the winner of each prime number game"""
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    ben = 0
    maria = 0
    lst = [1 for x in range(sorted(nums)[-1] + 1)]
    lst[0], lst[1] = 0, 0
    for a in range(2, len(lst)):
        for b in range(2, len(lst)):
            try:
                lst[b * a] = 0
            except (ValueError, IndexError):
                break
    for a in nums:
        if sum(lst[0:a + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None
