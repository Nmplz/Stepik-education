from typing import Any


class Note:
    __сyrillic_notes = "до", "ре", "ми", "фа", "соль", "ля", "си"

    def __init__(self, name, ton) -> None:
        self._name = name
        self._ton = ton

    def __setattr__(self, name: str, value: Any) -> None:
        if name == "_name":
            if value not in self.__сyrillic_notes:
                raise ValueError("недопустимое значение аргумента")

        if name == "_ton":
            if value not in [-1, 0, 1]:
                raise ValueError("недопустимое значение аргумента")
        super().__setattr__(name, value)


class Notes:
    __INSTANCES = None

    def __new__(cls):
        if cls.__INSTANCES is None:
            cls.__INSTANCES = super().__new__(cls)
        return cls.__INSTANCES

    __slots__ = ("_do", "_re", "_mi", "_fa", "_solt", "_la", "_si")

    def __init__(self) -> None:
        self._do = Note("до", 0)
        self._re = Note("ре", 0)
        self._mi = Note("ми", 0)
        self._fa = Note("фа", 0)
        self._solt = Note("соль", 0)
        self._la = Note("ля", 0)
        self._si = Note("си", 0)

    def __getitem__(self, item):
        return getattr(self, self.__slots__[item])

    def __setitem__(self, item, value):
        setattr(self, self.__slots__[item], value)
