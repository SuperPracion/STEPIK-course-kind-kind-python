class Track:
    def __init__(self, *args):
        self._points = list()
        if len(args) == 2:
            self._points.append(PointTrack(*args))
        else:
            for pt in args:
                self.add_back(pt)

    @property
    def points(self):
        return tuple(self._points)

    def add_back(self, pt):
        if isinstance(pt, PointTrack):
            self._points.append(pt)

    def add_front(self, pt):
        if isinstance(pt, PointTrack):
            self._points = [pt] + self._points[:]

    def pop_back(self):
        del self._points[-1]

    def pop_front(self):
        self._points.pop(0)

class PointTrack:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self.__value_validator(value)
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self.__value_validator(value)
        self._y = value

    @staticmethod
    def __value_validator(value):
        if type(value) not in (int, float):
            raise TypeError('координаты должны быть числами')
        return value

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"


tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
print(tr.points)
tr.pop_front()
for pt in tr.points:
    print(pt)