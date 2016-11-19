#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def is_empty(self):
        return len(self.elements) == 0


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, start, goal):
    """
    Get the distance between the start and the final node
    """
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.is_empty():
        current = frontier.get()

        if current == goal:
            break

        for next_item in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next_item)
            if next_item not in cost_so_far or new_cost < cost_so_far[next_item]:
                cost_so_far[next_item] = new_cost
                priority = new_cost + heuristic(goal, next_item)
                frontier.put(next_item, priority)
                came_from[next_item] = current

    return came_from, cost_so_far
