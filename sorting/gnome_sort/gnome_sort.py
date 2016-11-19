#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv
from random import randint

"""
Example usage:

>> time python3 gnome_sort.py 5000

real	0m5.385s
user	0m5.310s
sys	    0m0.041s
"""

try:
    k = int(argv[1])
except (IndexError, ValueError):
    k = 10

arr = [randint(1, 100) for x in range(k)]


def gnome_sort(collection):
    """
    Implementation of Gnome sort

    T(n) = O(n^2)
    """
    i = 1

    while i < len(collection):
        if not i or collection[i - 1] <= collection[i]:
            i += 1
        else:
            collection[i], collection[i - 1] = collection[i - 1], collection[i]
            i -= 1

    return collection


if __name__ == '__main__':
    print(arr)
    gnome_sort(arr)
    print(arr)
