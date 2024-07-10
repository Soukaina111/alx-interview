#!/usr/bin/python3

"""
Defines a function to calculate the minimum number of operations needed to form a string of 'n' 'H' characters.
Two operations are allowed: duplicating the entire string ('Copy All') and appending the last character to itself ('Paste').
If 'n' cannot be achieved, returns 0.
"""


def minOperations(n):
    """
    Calculates the minimum operations to form a string of 'n' 'H' characters.

    Parameters:
    - n: Desired length of the string.

    Returns:
    - Minimum number of operations required. Returns 0 if 'n' is unachievable.
    """
    if n <= 1:
        return 0

    remaining_length, divisor, operation_count = n, 2, 0

    while remaining_length > 1:
        if remaining_length % divisor == 0:
            remaining_length /= divisor
            operation_count += divisor
        else:
            divisor += 1

    return operation_count
