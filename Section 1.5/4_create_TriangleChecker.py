class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all(type(i) in (int, float) and i > 0 for i in self.__dict__.values()):
            return 1
        elif not (self.a + self.b > self.c) or not (self.b + self.c > self.a) or not (self.a + self.c > self.b):
            return 2
        else:
            return 3


a, b, c = map(int, input().split())  # эту строчку не менять
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())