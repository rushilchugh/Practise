__author__ = 'Rushil'


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if not self.root:
            self.root = Node(val)

        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.val:

            if node.left:                   #If a left Node exists
                self._add(val, node.left)
            elif not node.left:
                node.left = Node(val)

        if val > node.val:

            if node.right:                  #If a right Node exists
                self._add(val, node.right)
            elif not node.right:
                node.right = Node(val)











