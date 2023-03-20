class Validator:
    def __init__(self, min_value, max_value, type):
        self.min_value = min_value
        self.max_value = max_value
        self.type = type

    def __call__(self, value):
        if type(value) != self.type or not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')
        return value

class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value, float)


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value, int)


def is_valid(lst, validators):
    res = []
    for value in lst:
        for validator in validators:
            try:
                res.append(validator(value))
                break
            except:
                pass
    return res


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])  # [1, 4.5]
