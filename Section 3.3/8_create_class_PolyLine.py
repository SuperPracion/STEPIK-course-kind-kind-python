class PolyLine:
    def __init__(self, *args):
        self.points = [*args]

    def add_coord(self, x, y):
        self.points.append((x, y))

    def remove_coord(self, indx):
        try:
            del self.points[indx]
        except:
            pass

    def get_coords(self):
        return [coord for coord in self.points]

    def __len__(self):
        return len(self.points)

poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
a = poly.get_coords()
poly.add_coord(22, 33)
b = poly.get_coords()
poly.remove_coord(3)
c = poly.get_coords()

print(a)
print(b)
print(c)

