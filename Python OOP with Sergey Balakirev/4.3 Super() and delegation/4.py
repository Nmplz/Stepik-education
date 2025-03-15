class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func


# здесь объявляйте декоратор Callback
class Callback:
    def __init__(self, path, route_cls):
        self.path = path
        self.route_cls = route_cls

    # здесь нужные строчки

    def __call__(self, func):
        self.route_cls.add_callback(self.path, func)
        return func
