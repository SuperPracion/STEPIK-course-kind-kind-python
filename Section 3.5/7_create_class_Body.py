class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    @classmethod
    def __validate_value(cls,  other):
        return other if isinstance(other, (int, float)) else (other.ro * other.volume)


    def __eq__(self, other):
        m = self.__validate_value(other)
        return (self.ro * self.volume) == m

    def __lt__(self, other):
        m = self.__validate_value(other)
        return (self.ro * self.volume) < m

    def __gt__(self, other):
        m = self.__validate_value(other)
        return (self.ro * self.volume) > m
