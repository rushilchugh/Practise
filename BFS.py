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

    level = {S: 0}                      #Defining Source Node Level
    parent = {S: None}                  #Defining a Parent for each Node

    i = 1                               #Defining Initial Levels

    nodes_to_visit = [S]

    while nodes_to_visit:
        next_nodes = []

        for u in nodes_to_visit:
            neighbors = adjl[u]

            for v in neighbors:
                if v not in level.keys():
                    level[v] = i
                    parent[v] = u
                    next_nodes.append(v)

        nodes_to_visit = next_nodes
        i += 1

    return sorted(level.items(), key = lambda x: x[1]), parent

print(BFS(adj_list, "S"))





