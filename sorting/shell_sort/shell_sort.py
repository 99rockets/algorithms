#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv
from random import randint

"""
Example usage:

>> time python3 shell_sort.py 50000

real	0m0.559s
user	0m0.525s
sys	    0m0.016s
"""

try:
    k = int(argv[1])
except (IndexError, ValueError):
    k = 10

arr = [randint(1, 100) for x in range(k)]


def shell_sort(numbers):
    """
    Implementation of Shell sort
    """
    numbers_length = len(numbers)
    h = numbers_length // 2

    while h > 0:
        for i in range(numbers_length - h):
            j = i
            while j >= 0 and numbers[j] > numbers[j + h]:
                numbers[j], numbers[j + h] = numbers[j + h], numbers[j]
                j -= h
        h //= 2

    return numbers


if __name__ == '__main__':
    print(arr)
    print(shell_sort(arr))
