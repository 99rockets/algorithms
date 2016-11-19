#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv
from random import randint

"""
Example usage:

>> time python3 bucket_sort.py 5000

real	0m0.681s
user	0m0.658s
sys	    0m0.014s
"""

try:
    k = int(argv[1])
except (IndexError, ValueError):
    k = 10

arr = [randint(1, 100) for x in range(k)]


def bucket_sort(lst=None):
    """
    Implementation of Bucket sort
    """
    if lst is None:
        lst = []

    sorted_list = []
    list_lenth = max(lst) - min(lst) + 1
    bucket = [0] * list_lenth

    for item in lst:
        bucket[item - min(lst)] += 1

    for i in range(len(bucket)):
        if bucket[i] > 0:
            sorted_list.extend([(i + min(lst))] * bucket[i])

    return sorted_list


if __name__ == '__main__':
    print(arr)
    print(bucket_sort(arr))
