__author__ = 'Rushil'

adj_list = {
    "S": ["A", "X"],
    "A": ["S", "Z"],
    "X": ["S", "D", "C"],
    "Z": ["A"],
    "D": ["X", "C", "F"],
    "F": ["C", "V", "D"],
    "C": ["X", "D", "F"],
    "V": ["C", "F"],
}


def BFS(adjl, S):

    level = {S: 0}
    parent = {S: None}

    i = 1

    nodes_to_visit = [S]

    while nodes_to_visit:

        next_nodes = []

        for u in nodes_to_visit:
            neighbors = adjl[u]

            for v in neighbors:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next_nodes.append(v)

        nodes_to_visit = next_nodes
        i += 1

    return level, parent


a, b = BFS(adj_list, "S")

print(sorted(a.items(), key = lambda x: x[1]))