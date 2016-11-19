#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv
from random import randint
from collections import defaultdict

"""
Example usage:

>> time python3 counting_sort.py 50000

user    0.16s
system  0.02s
cpu     78%
total   0.221
"""

try:
    k = int(argv[1])
except (IndexError, ValueError):
    k = 10

arr = [randint(1, 100) for x in range(k)]


def counting_sort(lst, key=lambda x: x):
    """
    Implementation of counting sort
    """
    result = []
    count_dict = defaultdict(list)

    for i in lst:
        count_dict[key(i)].append(i)

    for j in range(min(count_dict), max(count_dict) + 1):
        result.extend(count_dict[j])

    return result


if __name__ == '__main__':
    print(arr)
    print(counting_sort(arr))
