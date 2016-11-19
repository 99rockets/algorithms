#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv
from random import randint

"""
Example usage:

>> time python3 odd_even_sort.py 5000

real	0m3.612s
user	0m3.576s
sys	    0m0.020s
"""

try:
    k = int(argv[1])
except (IndexError, ValueError):
    k = 10

arr = [randint(1, 100) for x in range(k)]


def odd_even_sort(numbers):
    """
    Implementation of odd-even sort

    Worst-case performance O(n^2)
    Best-case performance O(n)
    """
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for i in range(0, len(numbers) - 1, 2):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                is_sorted = False

        for i in range(1, len(numbers) - 1, 2):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                is_sorted = False

    return numbers


if __name__ == '__main__':
    print(arr)
    odd_even_sort(arr)
    print(arr)
