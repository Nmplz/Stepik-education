class TVProgram:
    def __init__(self, name):
        self.channel_name = name
        self.items = []

    def add_telecast(self, tl):
        if isinstance(tl, Telecast):
            self.items.append(tl)

    def remove_telecast(self, indx):
        for i in self.items:
            if indx == i.uid:
                self.items.remove(i)


class Telecast:

    @staticmethod
    def tele_check(number, name, duration):
        return (
            (isinstance(number, int) and number)
            and isinstance(name, str)
            and isinstance(duration, int)
        )

    def __init__(self, number, name, duration):
        if self.tele_check(number, name, duration):
            self.__id = number
            self.__name = name
            self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, id):
        if isinstance(id, int) and id:
            self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        if isinstance(duration, int):
            self.__duration = duration
