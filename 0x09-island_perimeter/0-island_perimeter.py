#!/usr/bin/python3
"""Defines island perimeter finding function."""


def island_perimeter(grid):
    """Return the perimiter of an island.
    The grid represents water by 0 and land by 1.
    Args:
        grid (list): A list of list of integers representing an island.
    Returns:
        The perimeter of the island defined in grid.
    """
    # Get the number of columns and rows in the grid
    num_columns = len(grid[0])
    num_rows = len(grid)
    # Initialize variables to keep track of the perimeter
    perimeter_edges = 0
    land_area = 0
    # Iterate through the grid
    row_index = 0
    while row_index < num_rows:
        column_index = 0
        while column_index < num_columns:
            # If the current cell is land (1)
            if grid[row_index][column_index] == 1:
                # Increment the land area
                land_area += 1
                # Check the left cell
                if (column_index > 0 and
                        grid[row_index][column_index - 1] == 1):
                    # If the left cell is also land, don't count the edge
                    perimeter_edges += 1
                # Check the top cell
                if (row_index > 0 and grid[row_index - 1][column_index] == 1):
                    # If the top cell is also land, don't count the edge
                    perimeter_edges += 1
            column_index += 1
        row_index += 1
    return land_area * 4 - perimeter_edges * 2
