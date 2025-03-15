class Singleton:
    is_instance = None
    is_singleton = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls.is_singleton is None:
                cls.is_singleton = super().__new__(cls)
            return cls.is_singleton

        if cls.is_instance is None:
            cls.is_instance = super().__new__(cls)
        return cls.is_instance


class Game(Singleton):
    def __init__(self, name):
        if "name" not in self.__dict__:
            self.name = name
