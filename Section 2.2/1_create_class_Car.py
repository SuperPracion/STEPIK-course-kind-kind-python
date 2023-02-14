class Car:
    def __init__(self):
        self.__model = ''

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if 2 <= len(value) <= 100 and isinstance(value, str):
            self.__model = value
