#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Return True if data is valid UTF-8 encoding"""
    count = 0
    for a in range(len(data)):
        if count == 0:
            bits = 0
            shift = 1 << 7
            while shift & data[a]:
                bits += 1
                shift = shift >> 1
            count = bits
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
        else:
            if not (data[a] & (1 << 7) and not (data[a] & (1 << 6))):
                return False
        count -= 1
    return count == 0
