__author__ = 'Rushil'

"""
MAX HEAP PROPERTY
For every node i other than the root, A[Parent(i)] > A[i], i.e. the parent node is greater than any child node
"""


# noinspection PyPep8Naming
class Heap(object):

    def __init__(self, val, left, right):
        self.val = val

    def getLeftIndex(self):
        return None