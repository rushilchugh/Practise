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

parent = {}

def DFS(adjl, V):

    global parent

    for S in V:                       #Iterating over Source vertices to visit all unconnected nodes
        if S not in parent:
            parent[S] = None
            DFS_Visit(adjl, S)


def DFS_Visit(adjl, S):

    global parent

    for v in adjl[S]:
        if v not in parent:
            parent[v] = S
            DFS_Visit(adjl, v)


DFS(adj_list, adj_list.keys())
