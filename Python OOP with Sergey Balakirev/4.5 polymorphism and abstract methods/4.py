from abc import ABC, abstractmethod


# здесь объявляйте классы


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return f"Базовый класс Model"


class ModelForm(Model):
    __ID = 0

    @classmethod
    def get_id(cls):
        cls.__ID += 1
        return cls.__ID

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self.__id = self.get_id()

    def get_pk(self):
        return self.__id
