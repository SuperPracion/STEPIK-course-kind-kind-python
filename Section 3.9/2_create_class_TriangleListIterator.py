class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        for row in range(len(self.lst)):
            for pos in range(row + 1):
                yield self.lst[row][pos]