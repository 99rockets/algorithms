#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import heapq
import bisect

from sys import argv
from random import randint

"""
Example usage:

>> time python3 patience_sort.py 5000

real	0m0.072s
user	0m0.054s
sys	    0m0.009s
"""

try:
    k = int(argv[1])
except (IndexError, ValueError):
    k = 10

arr = [randint(1, 100) for x in range(k)]


def patience_sort(sequence):
    """
    Implementation of Patience sort

    Worst-case performance O(n * log n)
    Best-case performance O(n) (occurs when the input is pre-sorted)
    """
    piles = []

    for x in sequence:
        new_pile = [x]
        i = bisect.bisect_left(piles, new_pile)
        if i != len(piles):
            piles[i].insert(0, x)
        else:
            piles.append(new_pile)

    print("longest increasing subsequence has length =", len(piles))

    # priority queue allows us to retrieve least pile efficiently
    for i in range(len(sequence)):
        small_pile = piles[0]
        sequence[i] = small_pile.pop(0)
        if small_pile:
            heapq.heapreplace(piles, small_pile)
        else:
            heapq.heappop(piles)

    assert not piles


if __name__ == '__main__':
    print(arr)
    patience_sort(arr)
    print(arr)
