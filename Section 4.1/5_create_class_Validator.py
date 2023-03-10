class Validator:
    def _is_valid(self, data):
        pass

    def __call__(self, *args, **kwargs):
        if self._is_valid(args[0]):
            return args[0]
        else:
            raise ValueError('данные не прошли валидацию')


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        super().__init__()
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if not isinstance(data, int):
            raise ValueError('данные не прошли валидацию')

        return True if self.min_value <= data <= self.max_value else False

class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        super().__init__()
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if not isinstance(data, float):
            raise ValueError('данные не прошли валидацию')

        return True if self.min_value <= data <= self.max_value else False


integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
#res2 = float_validator(10)    # исключение ValueError