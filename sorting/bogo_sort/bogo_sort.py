#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv
from random import randint, shuffle

"""
Example usage:

>> time python3 bogo_sort.py 5

user    0.04s
system  0.01s
cpu     86%
total   0.050

>> time python3 bogo_sort.py 10

user    77.95s
system  0.27s
cpu     99%
total   1:18.74
"""

try:
    k = int(argv[1])
except (IndexError, ValueError):
    k = 10

arr = [randint(1, 100) for x in range(k)]


def is_sorted(sequence):
    return not any(
        sequence[i] > sequence[i+1]
        for i in range(len(sequence)-1)
    )


def bogo_sort(sequence):
    """
    Implementation of Bogo sort (random sort)

    T(n) = O(n * n!)
    """
    while not is_sorted(sequence):
        shuffle(sequence)
    return sequence

if __name__ == '__main__':
    print(arr)
    print(bogo_sort(arr))
