#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv
from random import randint

"""
Example usage:

>> time python3 selection_sort.py 5000
user    1.62s
system  0.01s
cpu     98%
total   1.656
"""

try:
    k = int(argv[1])
except (IndexError, ValueError):
    k = 10

arr = [randint(1, 100) for x in range(k)]


def selection_sort(sequence):
    """
    Implementation of Selection sort

    T(n) = Θ(n2)
    """
    for i in range(len(sequence) - 1, 0, -1):
        max_position = 0

        for j in range(1, i + 1):
            if sequence[j] > sequence[max_position]:
                max_position = j

        tmp = sequence[i]
        sequence[i] = sequence[max_position]
        sequence[max_position] = tmp

    return sequence


if __name__ == '__main__':
    print(arr)
    print(selection_sort(arr))
