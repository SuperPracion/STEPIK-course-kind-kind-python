class CellException(Exception):
    pass


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass


class Cell:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, '_' + key, value)
        self._v = None

    @property
    def value(self):
        return self._v

    @value.setter
    def value(self, value):
        self._v = self._is_valid(value)

    def _is_valid(self, v):
        raise NotImplementedError()


class CellInteger(Cell):
    def __init__(self, min_value, max_value):
        super().__init__(min_value=min_value, max_value=max_value)

    def _is_valid(self, v):
        if self._min_value <= v or v <= self._max_value:
            raise CellIntegerException('значение выходит за допустимый диапазон')
        return v


class CellFloat(Cell):
    def __init__(self, min_value, max_value):
        super().__init__(min_value=min_value, max_value=max_value)

    def _is_valid(self, v):
        if self._min_value <= v or v <= self._max_value:
            raise CellFloatException('значение выходит за допустимый диапазон')
        return v


class CellString(Cell):
    def __init__(self, min_length, max_length):
        super().__init__(min_length=min_length, max_length=max_length)

    def _is_valid(self, v):
        if self._min_length >= len(v) or self._max_length <= len(v):
            raise CellStringException('значение выходит за допустимый диапазон')
        return v


class TupleData:
    def __init__(self, *args):
        for arg in args:
            if not isinstance(arg, CellInteger) and not isinstance(arg, CellFloat) and not isinstance(arg, CellString):
                raise TypeError()
        self.cells = [*args]

    def __getitem__(self, item):
        return self.cells[item]

    def __setitem__(self, key, value):
        self.cells[key] = value

    def __len__(self):
        return len(self.cells)

    def __iter__(self):
        for x in self.cells:
            yield x


t = TupleData(CellInteger(-10, 10), CellInteger(0, 2), CellString(5, 10))

d = (1, 0, 'sergey')
t[0] = d[0]
t[1] = d[1]
t[2] = d[2]
for i, x in enumerate(t):
    assert x == d[i], "объект класса TupleData хранит неверную информацию"

assert len(t) == 3, "неверное число элементов в объекте класса TupleData"

cell = CellFloat(-5, 5)
try:
    cell.value = -6.0
except CellFloatException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellFloatException"
#
cell = CellInteger(-1, 7)
try:
    cell.value = 8
except CellIntegerException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellIntegerException"
#
cell = CellString(5, 7)
try:
    cell.value = "hello world"
except CellStringException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellStringException"
#
assert issubclass(CellIntegerException, CellException) and issubclass(CellFloatException, CellException) and issubclass(
    CellStringException,
    CellException), "классы CellIntegerException, CellFloatException, CellStringException должны наследоваться от класса CellException"

