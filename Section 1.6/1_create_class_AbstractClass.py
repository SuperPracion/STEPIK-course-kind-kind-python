class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return f'Ошибка: нельзя создавать объекты абстрактного класса'

obj = AbstractClass()