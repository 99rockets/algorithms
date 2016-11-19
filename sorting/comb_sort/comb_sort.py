#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv
from random import randint

"""
Example usage:

>> time python3 comb_sort.py 5000

user    4.53s
system  0.04s
cpu     98%
total   4.613
"""

try:
    k = int(argv[1])
except (IndexError, ValueError):
    k = 10

arr = [randint(1, 100) for x in range(k)]


def comb_sort(lst):
    """
    Implementation of comb sort

    Worst-case performance: O(n^2)
    Best-case performance: O(n * log n)
    """
    f = round(len(lst) / 1.24733)

    while f >= 1:
        i = 0
        while i + f < len(lst):
            if lst[i] > lst[i+f]:
                lst[i], lst[i+f] = lst[i+f], lst[i]
            i += 1
        f -= 1
    return lst


if __name__ == '__main__':
    print(arr)
    comb_sort(arr)
    print(arr)
