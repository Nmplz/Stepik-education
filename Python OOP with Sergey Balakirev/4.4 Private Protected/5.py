# здесь объявляйте декоратор и все что с ним связано
def class_log(log):
    def decorator(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, class_log_decorated(v, log))
        return cls

    return decorator


def class_log_decorated(func, log):
    def wrapper(*args, **kwargs):
        log.append(func.__name__)
        return func(*args, **kwargs)

    return wrapper


vector_log = []  # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value
