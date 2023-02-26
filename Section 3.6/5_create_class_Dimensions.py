class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        self.__validate_value(value)
        object.__setattr__(self, key, value)

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    @staticmethod
    def __validate_value(value):
        if not type(value) in (int, float) or value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")


s_inp = input()  # эту строку (переменную s_inp) в программе не менять
lst_dims = sorted([Dimensions(*map(float, obj.split())) for obj in s_inp.split(';')], key=lambda x: hash(x))
