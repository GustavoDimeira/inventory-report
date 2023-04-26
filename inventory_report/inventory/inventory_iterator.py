from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.cicle = 0

    def __next__(self):
        if (self.cicle > len(self.data)):
            raise StopIteration
        self.cicle += 1
        return self.data[self.cicle - 1]
