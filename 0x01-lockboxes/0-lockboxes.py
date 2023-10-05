#!/usr/bin/python3
"""
Defines a function that determines if a box containing a list
of lists can be opened using keys stored in the lists
"""


def canUnlockAll(boxes):
    """
    Determines if boxes can be unlocked

    Args:
        boxes (list of list of int): A list of boxes,
        where each box is represented
        as a list of integers. Each integer represents a key to another box.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    position = 0  # Current position of the explorer
    unlocked = {}  # A dictionary to store unlocked boxes

    for box in boxes:
        if len(box) == 0 or position == 0:
            # If the box is empty or it's the first box,
            # mark it as "always_unlocked"
            unlocked[position] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != position:
                # If the key is valid and doesn't lead back to the current box,
                # mark it as unlocked
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            # If all boxes are unlocked, return True
            return True
        position += 1

    # If the loop completes and not all boxes are unlocked, return False
    return False
