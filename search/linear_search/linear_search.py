#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def linear_search(sequence, target):
    """
    Implementation of linear search algorithm

    T(n) = O(n)
    """
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return None


if __name__ == '__main__':
    lst = sorted([int(el) for el in input('Введите массив: ').split()])
    x = int(input('Введите искомый элемент: '))
    print('Искомый индекс:', linear_search(lst, x))
