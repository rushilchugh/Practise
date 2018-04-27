__author__ = 'Rushil'


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def add(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if not node.next:
            tm = Node(val)
            node.next = tm
            tm.prev = node
        else:
            self._add(val, node.next)

    def traverse(self, node):
        if node:
            print(node.val)
            self.traverse(node.next)

ll = LinkedList()
