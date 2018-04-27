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

V = adj_list.keys()

def DFS(adjl, V):                                       #V is the Vertex List

    parent = {}

    for S in V:                                         #Iterating for all Source Vertices in a set of Vertices
        if S not in parent.keys():                      #If it hasn't yet been visited, Visit and Mark the parent as None
            parent[S] = None
            DFS_Visit(adjl, S)                                #Recursivley Visit all the Vertices from this source vertex


def DFS_Visit(adjl, S):

    global parent

    for v in adjl[S]:
        if v not in parent.keys():
            parent[v] = S
            DFS_Visit(adjl, v)


DFS(adj_list, adj_list.keys())