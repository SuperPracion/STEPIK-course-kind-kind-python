class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.cell = cell
        self.ar = [cell(0) for _ in range(max_length)]

    def __getitem__(self, item):
        try:
            return self.ar[item].value
        except:
            raise ValueError('должно быть целое число')

    def __setitem__(self, key, value):
        if key > self.max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')

        self.ar[key].value = value

    def __str__(self):
        return ' '.join(map(str, [obj.value for obj in self.ar]))


class Integer:
    def __init__(self, start_value):
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if not isinstance(value, int):
            raise ValueError('должно быть целое число')
        self.__value = value


ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int)  # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
#ar_int[1] = 10.5  # должно генерироваться исключение ValueError
# ar_int[10] = 1  # должно генерироваться исключение IndexError
