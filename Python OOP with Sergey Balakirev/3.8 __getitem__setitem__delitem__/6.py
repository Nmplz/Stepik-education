class RadiusVector:
    def __init__(self, *args):
        for i in args:
            if not isinstance(i, (int, float)):
                raise AttributeError("Att should be int float")
        self.coords = list(args)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.coords[item]
        elif isinstance(item, slice):
            return tuple(self.coords[item])

    def __setitem__(self, key, value):
        if isinstance(key, int):
            self.coords[key] = value
        elif isinstance(key, slice):
            for i, v in enumerate(self.coords[key]):
                self.coords[i] = value[i]
