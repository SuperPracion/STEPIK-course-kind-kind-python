class Furniture:
    def __init__(self, name: str, weight):
        self._name = self.__verify_name(name)
        self._weight = self.__verify_weight(weight)

    def __verify_name(self, name):
        if not type(name) == str:
            raise TypeError('название должно быть строкой')
        return name

    def __verify_weight(self, weight):
        if not type(weight) in (int, float) or weight < 0:
            raise TypeError('вес должен быть положительным числом')
        return weight

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self.__verify_name(value)

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = self.__verify_weight(value)


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        return (self._tp, self._doors)


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height

    def get_attrs(self):
        return (self._height, )


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square

    def get_attrs(self):
        return (self._height, self._square)


cl = Closet('шкаф-купе', 342.56, True, 3)
print(cl._doors)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())
