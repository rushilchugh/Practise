__author__ = 'Rushil'


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if not self.root:
            t_node = Node(val)
            self.root = t_node
            t_node.parent = None

        else:
            self._add(val, self.root)

    def _add(self, val, node):

        if val < node.val:
            if not node.left:
                t_node = Node(val)
                node.left = t_node
                t_node.parent = node

            elif node.val:
                self._add(val, node.left)

        elif val > node.val:
            if not node.right:
                t_node = Node(val)
                node.right = t_node
                t_node.parent = node

            elif node.right:
                self._add(val, node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.val)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.val)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.val)
            self.inorder_traversal(node.right)

t = Tree()
a = [21, 4, 81, 69, 76, 54, 48, 66, 19, 34]

for i in a:
    t.add(i)

t.inorder_traversal(t.root)