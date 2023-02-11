import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


classes_list = [Line, Rect, Ellipse]
elements = []

for _ in range(217):
    r_class = random.choice(classes_list)
    if r_class == Line:
        elements.append(r_class(0, 0, 0, 0))
    else:
        elements.append(r_class(random.randint, random.randint, random.randint, random.randint))