#!/usr/bin/python3
""" This script calculates the minimum operations
required to generate a string of length 'n'
consisting entirely of 'H' characters.
"""


def min_operations(n: int) -> int:
    """
    Calculate the minimum operations needed to
    create a string of 'n' 'H' characters.

    Parameters:
    - n: An integer representing the desired length of the string.

    Returns:
    - An integer representing the minimum number of operations required.
    """
    next = 'H'
    mid = 'H'
    opera = 0
    st = len(mid)
    while (st < n):
        if n % st == 0:
            opera += 2
            next = mid
            mid += mid
        else:
            opera += 1
            mid += next
    if st != n:
        return 0
    return opera
