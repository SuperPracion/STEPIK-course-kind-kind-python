from math import sqrt


class IntFloat:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if type(value) not in (int, float) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")

        setattr(instance, self.name, value)


class Triangle:
    a = IntFloat()
    b = IntFloat()
    c = IntFloat()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.__check_value(a, b, c)

    def __check_value(self, a, b, c):
        if not ((a < b + c) and (b < a + c) and (c < a + b)):
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs):
        p = len(self)
        return sqrt(p / 2 * (p / 2 - self.a) * (p / 2 - self.b) * (p / 2 - self.c))
