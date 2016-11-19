#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv
from random import randint

"""
Example usage:

>> time python3 insertion_sort.py 5000
user    1.68s
system  0.01s
cpu     99%
total   1.708
"""

try:
    k = int(argv[1])
except (IndexError, ValueError):
    k = 10

arr = [randint(1, 100) for x in range(k)]


def insertion_sort(sequence):
    """
    Implementation of Insertion sort

    T(n) = a * n^2 + b * n + c
    T(n) = O(n^2)
    """
    for i in range(1, len(sequence)):
        value = sequence[i]
        j = i - 1

        while j >= 0 and sequence[j] > value:
            sequence[j+1] = sequence[j]
            j -= 1

        sequence[j+1] = value

    return sequence


if __name__ == '__main__':
    print(arr)
    print(insertion_sort(arr))
