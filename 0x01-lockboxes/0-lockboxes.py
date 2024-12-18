#!/usr/bin/python3
"""box numbered sequentially and each box may contain keys to other boxes"""


def canUnlockAll(boxes):
    """determine if all the boxes can be opened"""
    keyslist = [0]
    for a in keyslist:
        for b in boxes[a]:
            if b not in keyslist and b < len(boxes):
                keyslist.append(b)

    if len(keyslist) == len(boxes):
        return True
    else:
        return False
