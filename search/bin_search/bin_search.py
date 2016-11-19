#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def bin_search(sequence, x):
    """
    Binary search algorithm

    Worst-case performance O(log n)
    Best-case performance O(1)
    Average performance O(log n)
    """
    index = 0
    sequence_len = len(sequence)

    while sequence_len - index > 1:
        # Целочисленный тип в Python имеет неограниченную длину
        m = (index + sequence_len) // 2
        if x < sequence[m]:
            sequence_len = m
        else:
            index = m

    # если элемент не найден, возвращаем None
    return index if lst[index] == x else None


if __name__ == '__main__':
    lst = sorted([int(el) for el in input('Введите массив: ').split()])
    x = int(input('Введите искомый элемент: '))
    print('Искомый индекс:', bin_search(lst, x))
