class Planet:
    def __init__(self, name, diametr, period_solar, period):
        self._name = name
        self._diametr = diametr
        self._period_solar = period_solar
        self._period = period


class SolarSystem:
    __slots__ = ('_mercury', '_venus', '_earth', '_mars', '_jupiter', '_saturn', '_uranus', '_neptune')

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SolarSystem, cls).__new__(cls)

        return cls.instance

    def __init__(self):
        self._mercury = Planet('mercury', 4878, 87.97, 1407.5)
        self._venus = Planet('venus', 12104, 224.7, 5832.45)
        self._earth = Planet('earth', 12756, 365.3, 23.93)
        self._mars = Planet('mars', 6794, 687, 24.62)
        self._jupiter = Planet('jupiter', 142800, 4330, 9.9)
        self._saturn = Planet('saturn', 120660, 10753, 10.63)
        self._uranus = Planet('uranus', 51118, 30665, 17.2)
        self._neptune = Planet('neptune', 49528, 60150, 16.1)
