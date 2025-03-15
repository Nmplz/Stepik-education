class Museum:

    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        for i in self.exhibits:
            if i == obj:
                self.exhibits.remove(i)

    def get_info_exhibit(self, indx):
        for i, v in enumerate(self.exhibits):
            if i == indx:
                return v

    def get_info_exhibit(self, indx):
        for i, v in enumerate(self.exhibits):
            if i == indx:
                return f"Описание экспоната {v.name}: {v.descr}"


class Picture:
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr


class Mummies:
    def __init__(self, name, location, descr):
        self.name = name
        self.location = location
        self.descr = descr


class Papyri:
    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr
