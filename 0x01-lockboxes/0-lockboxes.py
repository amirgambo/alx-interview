#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Checks if all lockboxes can be unlocked.

    Args:
        boxes (list of list of int): A list of lists
        representing lockboxes and their keys.

    Returns:
        bool: True if all lockboxes can be unlocked; False otherwise.
    """

    # Initialize a set to keep track of keys we have.
    keys = set([0])

    # Initialize a set to keep track of visited boxes.
    visited = set()

    # Start with box 0.
    stack = [0]

    while stack:
        box = stack.pop()
        visited.add(box)

        for key in boxes[box]:
            if key not in keys:
                stack.append(key)
                keys.add(key)

    # Check if all boxes were visited.
    return len(visited) == len(boxes)


if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # False
