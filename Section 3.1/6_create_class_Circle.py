class Circle:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def radius(self):
        return self.__radius

    def __getattr__(self, item):
        return False

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            if key in ('_Circle__x', '_Circle__y'):
                object.__setattr__(self, key, value)
            elif key == '_Circle__radius' and value > 0:
                object.__setattr__(self, key, value)



assert type(Circle.x) == property and type(Circle.y) == property and type(
    Circle.radius) == property, "в классе Circle должны быть объявлены объекты-свойства x, y и radius"

try:
    cr = Circle(20, '7', 22)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при инициализации объекта с недопустимыми аргументами"

cr = Circle(20, 7, 22)
assert cr.x == 20 and cr.y == 7 and cr.radius == 22, "объекты-свойства x, y и radius вернули неверные значения"

cr.radius = -10  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
assert cr.radius == 22, "при присваивании некорректного значения, прежнее значение изменилось"

x, y = cr.x, cr.y
assert x == 20 and y == 7, "объекты-свойства x, y вернули некорректные значения"
assert cr.name == False, "при обращении к несуществующему атрибуту должно возвращаться значение False"

try:
    cr.x = '20'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"

cr.y = 7.8
cr.radius = 10.6
