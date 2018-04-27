__author__ = 'Rushil'

from Code2.graphs import adj_list_weighted

import heapq
import math


def Dijkstras(graph, s):

    S = []                          #Visited Vertices
    Q = []                          #Priority Queue

    parent = {s: None}

    d = {s: 0}

    for i in (graph.keys() - s):
        d[i] = math.inf

    heapq.heappush(Q, (0, s))

    while Q:

        distance, u = heapq.heappop(Q)

        curr_neighbors = graph[u].keys()

        for v in curr_neighbors:
            if d[v] > d[u] + graph[u][v]:
                d[v] = d[u] + graph[u][v]
                parent[v] = u

                heapq.heappush(Q, (d[v], v))

            else:
                pass

Dijkstras(adj_list_weighted, "a")