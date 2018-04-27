class Node:
    def __init__(self, X, Y):
        self.visited = False
        self.X = X
        self.Y = Y

class Grid:
    def __init__(self):
        self.nodes = []

        self.Rows = None
        self.Columns = None

        self.grid = None

        self.nFields = 0

    def takeInput(self):

        self.Rows, self.Columns = map(int, input().split())

        self.grid = [[Node(i, j) for j in range(self.Columns)] for i in range(self.Rows)]

        for i in range(self.Rows):
            CandyList = list(input().strip())

            for j, boolCandy in enumerate(CandyList):
                if boolCandy == "Y":
                    self.grid[i][j].visited = False
                    self.nodes.append(self.grid[i][j])

                elif boolCandy == "N":
                    self.grid[i][j].visited = True
                    self.nodes.append(self.grid[i][j])

    def DFSVisit(self):

        for node in self.nodes:

            if not node.visited:
                self.nFields += 1

                st = list()
                st.append(node)

                while st:
                    currNode = st.pop()

                    if not currNode.visited:
                        currNode.visited = True

                        if currNode.X < self.Rows - 1:
                            st.append(self.grid[currNode.X + 1][currNode.Y])

                        if currNode.X > 0:
                            st.append(self.grid[currNode.X - 1][currNode.Y])

                        if currNode.Y < self.Columns - 1:
                            st.append(self.grid[currNode.X][currNode.Y + 1])

                        if currNode.Y > 0:
                            st.append(self.grid[currNode.X][currNode.Y - 1])

        return 2 ** (self.nFields - 1)

a = Grid()
a.takeInput()
print(a.DFSVisit())

