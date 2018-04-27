__author__ = 'Rushil'


class Dictionary:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size


    def insert(self, item):
        pass

    def delete(self, item):
        pass

    def search(self, key):
        pass

    def hash(self, item):
        return item % self.size