class Aircraft:
    def __init__(self, model, mass, speed, top):
        self.model = model
        self.mass = mass
        self.speed = speed
        self.top = top

    @staticmethod
    def _str_valid(value):
        if type(value) != str:
            raise TypeError('неверный тип аргумента')
        return value

    @staticmethod
    def _pos_int_valid(value):
        if type(value) != int or 0 >= value:
            raise TypeError('неверный тип аргумента')
        return value

    @staticmethod
    def _pos_value(value):
        if type(value) not in (int, float) or 0 >= value:
            raise TypeError('неверный тип аргумента')
        return value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = self._str_valid(value)

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value):
        self._mass = self._pos_value(value)

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = self._pos_value(value)

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, value):
        self._top = self._pos_value(value)


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self.chairs = chairs

    @property
    def chairs(self):
        return self._chairs

    @chairs.setter
    def chairs(self, value):
        self._chairs = self._pos_int_valid(value)


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self.weapons = weapons

    @property
    def weapons(self):
        return self._weapons

    @weapons.setter
    def weapons(self, params):
        if type(params) != dict:
            raise TypeError('неверный тип аргумента')

        for key, value in params.items():
            self._str_valid(key)
            self._pos_int_valid(value)

        self._weapons = params


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140), PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}), WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]
