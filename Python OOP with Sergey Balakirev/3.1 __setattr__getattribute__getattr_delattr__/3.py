class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        for i, v in enumerate(self.modules):
            if i == indx:
                self.modules.remove(v)


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        if isinstance(lesson, LessonItem):
            self.lessons.append(lesson)

    def remove_lesson(self, indx):
        for i, v in enumerate(self.lessons):
            if i == indx:
                self.lessons.remove(v)


class LessonItem:
    atrrs = {"title": str, "practices": int, "duration": int}

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if (key in ["practices", "duration"] and isinstance(value, int)) or (
            key == "title" and isinstance(value, str)
        ):
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item == "title" or item == "practices" or item == "duration":
            raise AttributeError()
        else:
            object.__delattr__(self, item)
