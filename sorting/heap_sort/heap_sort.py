#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import heapq
from sys import argv
from random import randint

"""
Example usage:

>> time python3 heap_sort.py 5000

user    0.06s
system  0.01s
cpu     71%
total   0.091

>> time python3 heap_sort.py 50000

user    0.18s
system  0.02s
cpu     46%
total   0.410
"""

try:
    k = int(argv[1])
except (IndexError, ValueError):
    k = 10

arr = [randint(1, 100) for x in range(k)]


def heap_sort(lst):
    """
    Implementation of heap sort

    Worst-case performance: O(n * log n)
    """
    heapq.heapify(lst)
    lst[:] = [heapq.heappop(lst) for _ in range(len(lst))]

if __name__ == '__main__':
    print(arr)
    heap_sort(arr)
    print(arr)
