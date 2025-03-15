class Car:
    def __init__(self):
        self._model = None

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if isinstance(model, str) and 1 < len(model) < 100:
            self._model = model

    @model.deleter
    def model(self):
        del self._model
