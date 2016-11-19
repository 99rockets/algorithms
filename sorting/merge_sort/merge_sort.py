#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv
from random import randint

"""
Example usage:

>> time python3 merge_sort.py 5000
real	0m0.147s
user	0m0.128s
sys	    0m0.011s

>> time python3 merge_sort.py 50000
real	0m5.204s
user	0m5.159s
sys	    0m0.028s
"""

try:
    k = int(argv[1])
except (IndexError, ValueError):
    k = 10

arr = [randint(1, 100) for x in range(k)]


def merge_sort(sequence):
    """
    Implementation of Merge sort

    T(n) = 2T(n/2) + cn
    T(n) = cn * lgn + cn = Θ(n * lgn)
    """
    if len(sequence) <= 1:
        return sequence

    middle = int(len(sequence) / 2)
    left = merge_sort(sequence[:middle])
    right = merge_sort(sequence[middle:])
    return merge(left, right)


def merge(left, right):
    result = []
    
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    if len(left) > 0:
        result += left

    if len(right) > 0:
        result += right

    return result


if __name__ == '__main__':
    print(arr)
    print(merge_sort(arr))
