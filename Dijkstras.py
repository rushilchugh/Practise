__author__ = 'Rushil'

import math
import heapq


graph = {
          'a': {'b': 1, 'c':  4},
          'b': {'c':  2, 'd':  2, 'e':  2},
          'c': {},
          'd': {'b':  1, 'c':  5},
          'e': {'d': -2}
}


def Dijkstras(s, graph):
    d = {}
    P = {}

    d[s] = 0

    Q = []
    heapq.heappush(Q, (0, s))

    for i in (graph.keys() - s):
        d[i] = math.inf
        heapq.heappush(Q, (math.inf, i))

    S = [s]
    P = {s: None}

    while Q:
        elem = heapq.heappop(Q)
        u = elem[1]

        S.append(u)

        curr_neighbors = graph[u].keys()
        for v in curr_neighbors:

            curr_val = d[v]
            new_val = d[u] + graph[u][v]

            if curr_val > new_val:                      #if d[v] > d[u] + graph[u][v]:

                d[v] = new_val
                curr_val = new_val
                P[v] = u

                #Updating Priority Queue
                #i = Q.index((math.inf, v))
                i = [j[1] for j in Q].index(v)
                Q[i] = (d[v], v)

            else:
                pass

    return d, P, Q

print(Dijkstras('a', graph))