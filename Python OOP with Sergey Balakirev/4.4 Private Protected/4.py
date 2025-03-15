class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __setattr__(self, key, value):
        if key == "_model" and not type(value) == str:
            raise TypeError("неверный тип аргумента")
        if key == "_mass" and not value > 0:
            raise TypeError("неверный тип аргумента")
        if key == "_speed" and not value > 0:
            raise TypeError("неверный тип аргумента")
        if key == "_top" and not value > 0:
            raise TypeError("неверный тип аргумента")
        super().__setattr__(key, value)

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not isinstance(value, str):
            raise TypeError("неверный тип аргумента")
        self._model = value

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value):
        if not value > 0:
            raise TypeError("неверный тип аргумента")
        self._mass = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if not value > 0:
            raise TypeError("неверный тип аргумента")
        self._speed = value

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, value):
        if not value > 0:
            raise TypeError("неверный тип аргумента")
        self._top = value


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = chairs

    def __setattr__(self, key, value):
        if key == "_chairs":
            if not isinstance(value, int) or not value > 0:
                raise TypeError("неверный тип аргумента")
        super().__setattr__(key, value)

    @property
    def chairs(self):
        return self._chairs

    @chairs.setter
    def chairs(self, value):
        if not value > 0:
            raise TypeError("неверный тип аргумента")
        self._chairs = value


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons = weapons

    def __setattr__(self, key, value):

        if key == "_weapons":
            if not isinstance(
                value, dict
            ):  ##and all([type(x) == int for x in value.values()]):
                raise TypeError("неверный тип аргумента")
            else:
                if all((type(x) == int for x in value.values())):
                    super().__setattr__(key, value)
        super().__setattr__(key, value)

    @property
    def weapons(self):
        return self._weapons

    @weapons.setter
    def weapons(self, value):
        if not isinstance(value, dict):
            raise TypeError("неверный тип аргумента")
        for k, v in value.items():
            self._weapons[k] = v


planes = [
    PassengerAircraft("МС-21", 1250, 8000, 12000.5, 140),
    PassengerAircraft("SuperJet", 1145, 8640, 11034, 80),
    WarPlane("Миг-35", 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
    WarPlane("Су-35", 7034, 34000, 2400, {"ракета": 4, "бомба": 7}),
]
