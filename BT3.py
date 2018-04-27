__author__ = 'Rushil'


class Node:
    def __init__(self, key):
        self.val = key
        self.lc = None
        self.rc = None
        self.parent = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if not self.root:
            self.root = Node(val)

        else:
            self._add(self.root, val)

    def _add(self, node, val):

        if val > node.val:

            if node.rc:
                self._add(node.rc, val)
            else:
                tn = Node(val)
                node.rc = tn
                tn.parent = node.rc

        if val < node.val:
            if node.lc:
                self._add(node.lc, val)
            else:
                tn = Node(val)
                node.lc = tn
                tn.parent = node.lc

        if val == node.val:
            pass

    def in_traverse(self, node):
        if node:
            self.in_traverse(node.lc)
            print(node.val)
            self.in_traverse(node.rc)

    def pre_traverse(self, node):
        if node:
            print(node.val)
            self.pre_traverse(node.lc)
            self.pre_traverse(node.rc)

    def post_traverse(self, node):
        if node:
            self.post_traverse(node.lc)
            self.post_traverse(node.rc)
            print(node.val)
