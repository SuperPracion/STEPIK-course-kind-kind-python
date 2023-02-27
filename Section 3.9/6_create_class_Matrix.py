class Matrix:
    def __init__(self, rows_or_lst, cols=0, fill_value=0):
        if type(rows_or_lst) == list:
            self.rows = len(rows_or_lst)
            self.cols = len(rows_or_lst[0])
            if not all(len(r) == self.cols for r in rows_or_lst) or not all(self.__is_digit(x) for row in rows_or_lst for x in row):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')

            self.lst = rows_or_lst
        else:
            if type(rows_or_lst) != int or type(cols) != int or type(fill_value) not in (int, float):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

            self.rows = rows_or_lst
            self.cols = cols
            self.lst = [[fill_value for _ in range(cols)] for _ in range(rows_or_lst)]

    def __is_digit(self, value):
        return type(value) in (int, float)

    def __value_validator(self, value):
        r, c = value
        if not (0 <= r < self.rows) or not (0 <= c < self.cols):
            raise IndexError('недопустимые значения индексов')

    def __getitem__(self, item):
        self.__value_validator(item)
        return self.lst[item[0]][item[1]]

    def __setitem__(self, key, value):
        self.__value_validator(key)

        if not self.__is_digit(value):
            raise TypeError('значения матрицы должны быть числами')

        self.lst[key[0]][key[1]] = value

    def __check_dimensions(self, m):
        if self.rows != m.rows or self.cols != m.cols:
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __add__(self, other):
        if type(self) == type(other):
            self.__check_dimensions(other)
            return Matrix([[self[i, j] + other[i, j] for j in range(self.cols)] for i in range(self.rows)])
        else:
            self.__is_digit(other)
            return Matrix([[self[i, j] + other for j in range(self.cols)] for i in range(self.rows)])

    def __sub__(self, other):
        if type(self) == type(other):
            self.__check_dimensions(other)
            return Matrix([[self[i, j] - other[i, j] for j in range(self.cols)] for i in range(self.rows)])
        else:
            self.__is_digit(other)
            return Matrix([[self[i, j] - other for j in range(self.cols)] for i in range(self.rows)])