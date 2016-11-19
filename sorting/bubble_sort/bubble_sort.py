#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv
from random import randint

"""
Example usage:

>> time python3 bubble_sort.py 5000

user    3.37s
system  0.02s
cpu     99%
total   3.398
"""

try:
    k = int(argv[1])
except (IndexError, ValueError):
    k = 10

arr = [randint(1, 100) for x in range(k)]


def bubble_sort(sequence):
    """
    Implementation of Bubble sort

    T(n) = O(n^2)
    """
    for i in reversed(range(len(sequence))):
        for j in range(1, i + 1):
            if sequence[j-1] > sequence[j]:
                sequence[j], sequence[j-1] = sequence[j-1], sequence[j]
    return sequence


if __name__ == '__main__':
    print(arr)
    print(bubble_sort(arr))
