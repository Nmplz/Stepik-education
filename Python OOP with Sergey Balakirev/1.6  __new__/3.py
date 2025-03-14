TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"

    def __init__(self, name):
        self.name = name


class DialogLinux:
    name_class = "DialogLinux"

    def __init__(self, name):
        self.name = name


class Dialog:
    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            return DialogWindows(*args, **kwargs)
        elif TYPE_OS == 2:
            return DialogLinux(*args, **kwargs)
        else:
            return "Не удалось создать объект класса"
