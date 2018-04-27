#from collections import defaultdict
#
#def numberOfBreaks(graph):
#    bks = [0]
#    visited = set()
#    def recur(i):
#        visited.add(i)
#        if len(graph[i]) == 1 and graph[i][0] in visited:
#            return 1
#        children = 0
#        for x in graph[i]:
#            if x not in visited:
#                y = recur(x)
#                if y % 2 == 0:
#                    bks[0] += 1
#                else:
#                    children += y
#        return children + 1
#
#    recur(graph.keys().next())
#    return bks[0]
#
#def main():
#    n, m = map(int, input().split())
#    edges = defaultdict(list)
#    for _ in range(m):
#        p, q = map(int, input().split())
#        edges[p].append(q)
#        edges[q].append(p)
#    print(numberOfBreaks(edges))
#
#main()


class Node(object):
    def __init__(self, data):
        self.data=data
        self.children=[]
    def add_child(self,obj):
        self.children.append(obj)

class Tree:
    def __init__(self):
        self.nodes={}
    def add_node(self,data,parent=None):
        node=Node(data)
        self.nodes[data]=node
        if parent is not None:
            self.nodes[parent].add_child(data)
        return node
    def traverse(self, data):
        yield data
        queue = self.nodes[data].children
        while queue:
            yield queue[0]
            expansion = self.nodes[queue[0]].children
            queue = expansion+queue[1:]                      #bfs traversal

inputs=[int(i) for i in input().split()]
connected_edges=[]
total_vertices=set()
for i in range(inputs[1]):
    pair_of_vertices=[int(j) for j in input().split()]
    connected_edges.append(pair_of_vertices)
tree=Tree()
for i in connected_edges:
    if connected_edges.index(i)==0:
        m=min(i)
        tree.add_node(m)
    total_vertices.add(i[0])
    total_vertices.add(i[1])
    tree.add_node(i[0], i[1])
child_nodes_of_each_node=[]
count=0
for j in list(total_vertices)[1:]:
    gen=tree.traverse(j)
    for i in gen:
        count += 1
    child_nodes_of_each_node.append(count)
    count=0
nof_cut_edges=len([i for i in child_nodes_of_each_node if i%2==0 and i!=1])
print(nof_cut_edges)
