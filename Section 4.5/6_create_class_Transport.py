from abc import ABC, abstractmethod


class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Country(CountryInterface):
    def __init__(self, name, population, square):
        self.name = name
        self.population = population
        self.square = square

    @property
    def name(self):
        return self._name

    @property
    def population(self):
        return self._population

    @property
    def square(self):
        return self._square

    @name.setter
    def name(self, value):
        self._name = value

    @population.setter
    def population(self, value):
        self._population = value

    @square.setter
    def square(self, value):
        self._square = value

    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"


country = Country("Россия", 140000000, 324005489.55)
print(country.get_info())
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info()) # Россия: 354005483.0, 150000000