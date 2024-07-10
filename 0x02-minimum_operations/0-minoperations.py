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
    if n <= 1:
        return 0
    num, idx, opera = n, 2, 0

    while num > 1:
        if num % idx == 0:
            num = num / idx
            opera = opera + idx
        else:
            idx += 1
    return opera
