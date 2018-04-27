__author__ = 'Rushil'

from Code2.graphs import adj_list


def BFS(adj_list, S):

    parent = {S: None}
    level = {S: 0}

    i = 1

    nodes_to_visit = [S]

    while nodes_to_visit:
        next_nodes = []

        for u in nodes_to_visit:
            neighbors = adj_list[u]

            for v in neighbors:
                if v not in parent.keys():
                    parent[v] = u
                    level[v] = i
                    next_nodes.append(v)

        nodes_to_visit = next_nodes
        i += 1

    return parent, level

print(BFS(adj_list, "S"))