class Node:
    def __init__(self, X, Y):
        self.visited = False
        self.X = X
        self.Y = Y

    def __repr__(self):
        return "Node({0}-{1}, {2})".format(self.visited, self.X, self.Y)

class Grid:
    def __init__(self):
        self.nodes = []

        self.R = None
        self.C = None

        self.grid = None

        self.fields = 0

    def takeInput(self):

        self.R, self.C = map(int, input().split())

        self.grid = [[Node(i, j) for j in range(self.C)] for i in range(self.R)]

        for i in range(self.R):
            ifCanList = list(input().strip())

            for j, ifCan in enumerate(ifCanList):
                if ifCan == "Y":
                    self.grid[i][j].visited = False
                    self.nodes.append(self.grid[i][j])

                elif ifCan == "N":
                    self.grid[i][j].visited = True
                    self.nodes.append(self.grid[i][j])

    def showGrid(self):
        for i in self.grid:
            print(i)

    def DFS(self):

        for node in self.nodes:

            if not node.visited:
                self.fields += 1

                st = list()
                st.append(node)

                while st:
                    currNode = st.pop()

                    if not currNode.visited:
                        currNode.visited = True

                        if currNode.X < self.R - 1:
                            st.append(self.grid[currNode.X + 1][currNode.Y])

                        if currNode.X > 0:
                            st.append(self.grid[currNode.X - 1][currNode.Y])

                        if currNode.Y < self.C - 1:
                            st.append(self.grid[currNode.X][currNode.Y + 1])

                        if currNode.Y > 0:
                            st.append(self.grid[currNode.X][currNode.Y - 1])

        return 2 ** (self.fields - 1)

a = Grid()
a.takeInput()
print(a.DFS())
