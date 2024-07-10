#!/usr/bin/python3
"""
ALX- interview Minimum Operations
"""


def minOperations(n: int) -> int:
    """
    Minimum Operations needed to get n H characters.

    Args:
        n (int): The target number of H characters to achieve.

    Returns:
        int: The minimum number of operations needed to get n H characters.
        If the target number is impossible to achieve, it returns 0.
    """
    current_num_H = 'H'  # Start with a single 'H' character
    clipboard_contents = 'H'  # Initially, the clipboard contains a single 'H'
    num_operations = 0  # Initialize the number of operations to 0

    # Iterate until the current number of H characters is equal to the target
    for _ in range(n):
        if n % len(current_num_H) == 0:
            # Copy all the H characters and paste them
            num_operations += 2
            clipboard_contents = current_num_H
            current_num_H += current_num_H
        else:
            # Copy and paste one more H character
            num_operations += 1
            current_num_H += clipboard_contents

    # If the final number of H characters is not equal to the target, return 0
    if len(current_num_H) != n:
        return 0

    return num_operations
