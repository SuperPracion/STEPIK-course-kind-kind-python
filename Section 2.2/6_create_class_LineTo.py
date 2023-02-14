import math


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):
        self.lines = [LineTo(0, 0), *args]

    def get_path(self):
        return self.lines

    def get_length(self):
        back = self.lines[0]
        sum = 0
        for line in self.lines[1:]:
            sum += math.sqrt((line.x - back.x) ** 2 + (line.y - back.y) ** 2)
            back = line

        return sum

    def add_line(self, line):
        self.lines.append(line)


# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))
# dist = p.get_length()

p = PathLines(LineTo(1, 2))
print(p.get_length())  # 2.23606797749979
p.add_line(LineTo(10, 20))
p.add_line(LineTo(5, 17))
print(p.get_length())  # 28.191631669843197
m = p.get_path()
print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True

h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
print(h.get_length())  # 71.8992593599813

k = PathLines()
print(k.get_length())  # 0
print(k.get_path())  # []