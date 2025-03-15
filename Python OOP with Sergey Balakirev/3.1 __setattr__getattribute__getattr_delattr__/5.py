class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        if type(app) not in [type(x) for x in self.apps]:
            self.apps.append(app)

    def remove_app(self, app):
        if app in self.apps:
            self.apps.remove(app)


class AppVK:
    def __init__(self, name="ВКонтакте"):
        self.name = name


class AppYouTube:
    def __init__(self, memory_max=1024):
        self.name = "YouTube"
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list):
        self.name = "Phone"
        self.phone_list = phone_list
