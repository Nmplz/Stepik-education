from abc import ABC, abstractmethod


class CountryInterface(ABC):

    @property
    @abstractmethod
    def name(self):
        return

    @name.setter
    def name(self, value):
        pass

    @property
    @abstractmethod
    def population(self):
        return

    @population.setter
    def population(self, value):
        pass

    @property
    @abstractmethod
    def square(self):
        return

    @square.setter
    def square(self, value):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Country(CountryInterface):

    def __init__(self, name, population, square):
        self._name = name
        self._population = population
        self._square = square

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, value):
        self._square = value

    def get_info(self):
        return f"{self._name}: {self._square}, {self._population}"
