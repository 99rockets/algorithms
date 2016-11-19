#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from sys import argv
from random import randint

"""
Example usage:

>> time python3 stooge_sort.py 50

real	0m0.062s
user	0m0.048s
sys	    0m0.008s
"""

try:
    k = int(argv[1])
except (IndexError, ValueError):
    k = 10

arr = [randint(1, 100) for x in range(k)]


def stooge_sort(collection, i=None, j=None):
    """
    Implementation of Stooge sort

    T(n) = O(n^2.71)
    """
    if i is None:
        i = 0

    if j is None:
        j = len(collection) - 1

    if collection[i] > collection[j]:
        collection[i], collection[j] = collection[j], collection[i]

    if i + 1 >= j:
        return

    param = math.floor((j - i + 1) / 3)

    # First two-thirds
    stooge_sort(collection, i, j - param)
    # Last two-thirds
    stooge_sort(collection, i + param, j)
    # First two-thirds again
    stooge_sort(collection, i, j - param)


if __name__ == '__main__':
    print(arr)
    stooge_sort(arr)
    print(arr)
