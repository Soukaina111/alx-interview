#!/usr/bin/python3
"""
0x01. Lockboxes
"""
def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list of lists, where each inner list represents the keys inside a box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    nm = len(boxes)
    visited = [False] * nm
    visited[0] = True  # The first box is unlocked by default

    pointer = [0]  # Start with the first box

    while pointer:
        current_box = pointer.pop(0)

        for key in boxes[current_box]:
            if key < nm and not visited[key]:
                visited[key] = True
                pointer.append(key)

    return all(visited)
