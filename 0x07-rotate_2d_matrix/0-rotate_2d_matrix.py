#!/usr/bin/python3
""" Rotate 2D Matrix
A script to demonstrate rotating a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix, rotate it 90 degrees clockwise
        Args:
        matrix (list of lists): An n x n 2D matrix to be rotated.

        Modifies the original matrix in place to save memory.
    """
    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list(y)

    if __name__ == '__main__':
        # Define a sample 3x3 matrix
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        # Call the rotate_2d_matrix function to rotate the matrix
        rotate_2d_matrix(matrix)
        # Print the rotated matrix to verify the result
        print(matrix)
