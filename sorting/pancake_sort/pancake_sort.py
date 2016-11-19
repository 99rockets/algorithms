#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv
from random import randint

"""
Example usage:

>> time python3 pancake_sort.py 5000

real	0m3.555s
user	0m3.499s
sys	    0m0.031s
"""

try:
    k = int(argv[1])
except (IndexError, ValueError):
    k = 10

arr = [randint(1, 100) for x in range(k)]


def flip(collection, i, j):
    tmp = collection[i:j+1]
    tmp = tmp[::-1]
    collection[i:j+1] = tmp
    return collection


def pancake_sort(collection):
    """
    Implementation of Pancake sort
    """
    sorted_index = -1

    while sorted_index != len(collection) - 1:
        max_unsorted = sorted_index + 1

        for i in range(sorted_index + 2, len(collection)):
            if collection[i] >= collection[max_unsorted]:
                max_unsorted = i

        if max_unsorted < len(collection) - 1:
            collection = flip(collection, max_unsorted, len(collection))
        elif max_unsorted == len(collection) - 1:
            collection = flip(collection, sorted_index + 1, len(collection) - 1)
            sorted_index += 1

    return collection.reverse()


if __name__ == '__main__':
    print(arr)
    pancake_sort(arr)
    print(arr)
