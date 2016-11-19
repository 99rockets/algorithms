#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque


graph_tasks = {
    "wash the dishes": ["have lunch"],
    "cook food": ["have lunch"],
    "have lunch": [],
    "wash laundry": ["dry laundry"],
    "dry laundry": ["fold laundry"],
    "fold laundry": []
}

graph_numbers = {
    0: [1, 2],
    1: [3, 4],
    2: [],
    3: [],
    4: [],
    5: [6, 7],
    6: [],
    7: []
}


def kahn_topological_sort(graph):
    """
    Implementation of topological sort on a graph - Kahn's algorithm
    """
    # determine in-degree
    in_degree = {u: 0 for u in graph}

    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # collect nodes with zero in-degree
    Q = deque()

    for u in in_degree:
        if in_degree[u] == 0:
            Q.appendleft(u)

    # list for order of nodes
    L = []

    while Q:
        # choose node of zero in-degree and 'remove' it from graph
        u = Q.pop()
        L.append(u)

        for v in graph[u]:
            in_degree[v] -= 1

            if in_degree[v] == 0:
                Q.appendleft(v)

    if len(L) == len(graph):
        return L
    else:
        # if there is a cycle, then return an empty list
        return []


def dfs_topological_sort(graph):
    """
    Implementation of topological sort on a graph -
    DFS (depth first search) algorithm
    """
    # recursive dfs with additional list for order of nodes
    L = []
    color = {u: "white" for u in graph}
    found_cycle = [False]

    for u in graph:
        if color[u] == "white":
            dfs_visit(graph, u, color, L, found_cycle)
        if found_cycle[0]:
            break

    if found_cycle[0]:
        # if there is a cycle, then return an empty list
        L = []

    L.reverse()
    return L


def dfs_visit(graph, u, color, L, found_cycle):
    if found_cycle[0]:
        return

    color[u] = "gray"

    for v in graph[u]:
        if color[v] == "gray":
            found_cycle[0] = True
            return
        if color[v] == "white":
            dfs_visit(graph, v, color, L, found_cycle)

    color[u] = "black"
    # when we're done with u, add u to list (reverse it later!)
    L.append(u)


if __name__ == '__main__':
    print("\n Topological sorts for tasks graph")

    print("\n *** Kahn's algorithm:")

    for task in kahn_topological_sort(graph_tasks):
        print(task)

    print('\n *** Modified DFS:')

    for task in dfs_topological_sort(graph_tasks):
        print(task)

    print("\n Topological sorts for numbers graph")

    print("\n *** Kahn's algorithm:")

    print(kahn_topological_sort(graph_numbers))

    print('\n *** Modified DFS:')

    print(dfs_topological_sort(graph_numbers))
