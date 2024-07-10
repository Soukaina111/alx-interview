#!/usr/bin/python3
""" This script calculates the minimum operations
required to generate a string of length 'n'
consisting entirely of 'H' characters.
"""

def min_operations(n: int) -> int:
    """
    Calculate the minimum operations needed to create a string of 'n' 'H' characters.

    Parameters:
    - n: An integer representing the desired length of the string.

    Returns:
    - An integer representing the minimum number of operations required.
    """
    next_char = 'H'
    accumulated_string = 'H'
    operation_count = 0

    # Loop until the accumulated string reaches the target length 'n'.
    while len(accumulated_string) < n:
        if n % len(accumulated_string) == 0:
            operation_count += 2
            next_char = accumulated_string
            accumulated_string += accumulated_string
        else:
            operation_count += 1
            accumulated_string += next_char

    if len(accumulated_string) != n:
        return 0

    return operation_count
