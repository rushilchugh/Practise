__author__ = 'Rushil'

from Code2.graphs import adj_list

parent = {}
visited = []


def DFS(adj_list):

    vertices = adj_list.keys()

    for v in vertices:

        if v not in visited:
            parent[v] = None
            visited.append(v)
            DFS_traverse(adj_list, v)


def DFS_traverse(adj_list, S):

    neighbors = adj_list[S]

    for u in neighbors:

        if u not in visited:
            parent[u] = S
            visited.append(u)
            DFS_traverse(adj_list, u)


DFS(adj_list)

print(parent)