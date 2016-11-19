#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from sys import argv
from random import randint

"""
Example usage:

>> time python3 radix_sort.py 50000

real	0m0.500s
user	0m0.460s
sys	    0m0.018s
"""

try:
    k = int(argv[1])
except (IndexError, ValueError):
    k = 10

arr = [randint(1, 100) for x in range(k)]


def radix_sort(numbers):
    """
    Implementation of Radix sort
    """
    list_length = len(numbers)

    if list_length == 0:
        return numbers

    number_length = get_number_length(max(numbers))

    for i in range(1, number_length + 1):
        sort_on_digit(numbers, i)


def get_number_length(number):
    if number == 0:
        return 1
    else:
        return int(math.log(number, 10)) + 1


def sort_on_digit(numbers, i):
    k = 9
    c = [0] * (k + 1)
    a = numbers[:]
    digits = []

    for j in range(0, len(numbers)):
        digit = get_digit(a[j], i)
        digits.append(digit)
        c[digit] += 1

    for j in range(1, k + 1):
        c[j] += c[j - 1]

    for j in range(len(numbers) - 1, -1, -1):
        digit = digits[j]
        numbers[c[digit] - 1] = a[j]
        c[digit] -= 1


def get_digit(number, i):
    if i > get_number_length(number):
        return 0
    else:
        return int(str(number)[-i])


if __name__ == '__main__':
    print(arr)
    radix_sort(arr)
    print(arr)
