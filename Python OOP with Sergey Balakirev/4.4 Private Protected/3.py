class Observer:
    def update(self, data):
        pass

    def __hash__(self):
        return hash(id(self))


class Subject:
    def __init__(self):
        self.__observers = {}
        self.__data = None

    def add_observer(self, observer):
        self.__observers[observer] = observer

    def remove_observer(self, observer):
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self):
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data):
        self.__data = data
        self.__notify_observer()


class Data:
    def __init__(self, temp, press, wet):
        self.temp = temp  # температура
        self.press = press  # давление
        self.wet = wet  # влажность


# здесь объявляйте дочерние классы TemperatureView, PressureView и WetView
class TemperatureView(Observer):
    def update(self, data):
        return f"Текущая температура {data.temp}"


class PressureView(Observer):
    def update(self, data):
        return f"Текущее давление {data.press}"


class WetView(Observer):
    def update(self, data):
        return f"Текущая влажность {data.wet}"
