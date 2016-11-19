#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv
from random import randint

"""
Example usage:

>> time python3 cocktail_sort.py 5000

real	0m3.505s
user	0m3.451s
sys	    0m0.029s
"""

try:
    k = int(argv[1])
except (IndexError, ValueError):
    k = 10

arr = [randint(1, 100) for x in range(k)]


def cocktail_sort(lst):
    """
    Implementation of Cocktail sort
    """
    left = 0
    right = len(lst) - 1

    while left <= right:
        for i in range(left, right, +1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        right -= 1

        for i in range(right, left, -1):
            if lst[i - 1] > lst[i]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
        left += 1

    return lst


if __name__ == '__main__':
    print(arr)
    print(cocktail_sort(arr))
