#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sequential_search(sequence, target):
    """
    Implementation of Sequential search algorithm
    """
    position = 0
    is_found = False

    while position < len(sequence) and not is_found:
        if sequence[position] == target:
            is_found = True
        else:
            position += 1

    if is_found:
        return position

    return None


if __name__ == '__main__':
    test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequential_search(test_list, 3))
    print(sequential_search(test_list, 13))
    print(sequential_search(test_list, 1))
    print(sequential_search(test_list, 32))
