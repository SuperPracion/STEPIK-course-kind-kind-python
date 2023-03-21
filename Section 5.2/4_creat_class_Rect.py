class Rect:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        if key in ('_height', '_width') and value <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        object.__setattr__(self, key, value)

    def is_collision(self, rect):
        if not isinstance(rect, Rect):
            pass

        if not (self._x + self._width < rect._x or rect._x + rect._width < self._x or self._y + self._height < rect._y or rect._y + rect._height < self._y):
            raise TypeError('прямоугольники пересекаются')


def is_collision(rect_1, rect_2):
    try:
        rect_1.is_collision(rect_2)
    except:
        return True
    return False


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
lst_not_collision = [rect_1 for rect_1 in lst_rect if
                     not any(is_collision(rect_1, rect_2) for rect_2 in lst_rect if rect_1 != rect_2)]
