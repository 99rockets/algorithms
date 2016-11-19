#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv
from random import randint

"""
Example usage:

>> time python3 stupid_sort.py 500

real	0m2.752s
user	0m2.716s
sys	    0m0.021s
"""

try:
    k = int(argv[1])
except (IndexError, ValueError):
    k = 10

arr = [randint(1, 100) for x in range(k)]


def stupid_sort(collection):
    """
    Implementation of Stupid sort

    T(n) = O(n^3)
    """
    i = 0
    n = len(collection) - 1

    while i < n:
        if collection[i + 1] < collection[i]:
            collection[i], collection[i + 1] = collection[i + 1], collection[i]
            i = 0
        else:
            i += 1
    return collection


if __name__ == '__main__':
    print(arr)
    stupid_sort(arr)
    print(arr)
