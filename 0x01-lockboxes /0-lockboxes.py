#!/usr/bin/python3
"""Solves the lock boxes puzzle"""


def look_next_opened_box(opened_boxes):
    """Looks for the next opened box
    Args:
        opened_boxes (dict): Dictionary which contains boxes already opened
    Returns:
        tuple: Index of the next opened box and its keys
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            return index, box.get('keys')
    return None, None


def canUnlockAll(boxes):
    """Check if all boxes can be opened
    Args:
        boxes (list): List which contain all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    opened_boxes = {0: {'status': 'opened', 'keys': boxes[0]}}
    opened_set = {0}

    while True:
        index, keys = look_next_opened_box(opened_boxes)
        if keys is None:
            break
        opened_boxes[index]['status'] = 'opened/checked'
        for key in keys:
            if key not in opened_set and key < len(boxes):
                opened_boxes[key] = {'status': 'opened', 'keys': boxes[key]}
                opened_set.add(key)

    return len(opened_set) == len(boxes)


def main():
    """Entry point"""
    print(canUnlockAll([[1], [2], [3], [4], []]))  # Example test case


if __name__ == '__main__':
    main()
