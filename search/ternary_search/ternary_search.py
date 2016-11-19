#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def ternary_search_recursion(f, left, right, absolute_precision):
    """
    Implementation of Ternary search algorithm (recursive version);

    left and right are the current bounds;
    the maximum is between them;
    """
    if abs(right - left) < absolute_precision:
        return (left + right) / 2

    left_third = (2 * left + right) / 3
    right_third = (left + 2 * right) / 3

    if f(left_third) < f(right_third):
        return ternary_search_recursion(
            f, left_third, right, absolute_precision)
    else:
        return ternary_search_recursion(
            f, left, right_third, absolute_precision)


def ternary_search_iter(f, left, right, absolute_precision):
    """
    Implementation of Ternary search algorithm (iterative version)

    Find maximum of unimodal function f() within [left, right]
    To find the minimum, revert the if/else statement or revert the comparison.
    """
    while True:
        # left and right are the current bounds; the maximum is between them
        if abs(right - left) < absolute_precision:
            return (left + right) / 2

        left_third = left + (right - left) / 3
        right_third = right - (right - left) / 3

        if f(left_third) < f(right_third):
            left = left_third
        else:
            right = right_third
