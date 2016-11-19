#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv
from random import randint

"""
Example usage:

>> time python3 quick_sort.py 5000

user    0.09s
system  0.01s
cpu     91%
total   0.114

>> time python3 quick_sort.py 50000

user    2.14s
system  0.02s
cpu     97%
total   2.217
"""

try:
    k = int(argv[1])
except (IndexError, ValueError):
    k = 10

arr = [randint(1, 100) for x in range(k)]


def quick_sort(sequence):
    """
    Implementation of Quicksort

    Worst case is O(n^2)
    Average case is O(n * log n)
    Performance depends largely on Pivot selection
    """
    quick_sort_helper(sequence, 0, len(sequence) - 1)


def quick_sort_helper(sequence, first, last):
    if first < last:
        split_point = partition(sequence, first, last)
        quick_sort_helper(sequence, first, split_point - 1)
        quick_sort_helper(sequence, split_point + 1, last)


def partition(sequence, first, last):
    pivot = sequence[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and sequence[left_mark] <= pivot:
            left_mark += 1

        while sequence[right_mark] >= pivot and right_mark >= left_mark:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            tmp = sequence[left_mark]
            sequence[left_mark] = sequence[right_mark]
            sequence[right_mark] = tmp

    tmp = sequence[first]
    sequence[first] = sequence[right_mark]
    sequence[right_mark] = tmp

    return right_mark


if __name__ == '__main__':
    print(arr)
    quick_sort(arr)
    print(arr)
