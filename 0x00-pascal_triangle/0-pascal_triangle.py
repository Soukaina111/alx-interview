#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Returns a list of integers representing the Pascal Triangle of n.
    Returns an empty list if n <= 0( n will be always an integer).
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        current_row = [1]
        previous_row = triangle[-1]
        for i in range(len(previous_row) - 1):
            current_row.append(previous_row[i] + previous_row[i + 1])
        current_row.append(1)
        triangle.append(current_row)

    return triangle
