class PrimaryKeyError(Exception):
    def __init__(self, id=None, pk=None):
        if id is None and pk is None:
            self.message = "Первичный ключ должен быть целым неотрицательным числом"
        elif id is not None:
            self.message = f"Значение первичного ключа id = {id} недопустимо"
        elif pk is not None:
            self.message = f"Значение первичного ключа pk = {pk} недопустимо"
        super().__init__(self.message)


# Пример использования:
try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as e:
    print(e)
