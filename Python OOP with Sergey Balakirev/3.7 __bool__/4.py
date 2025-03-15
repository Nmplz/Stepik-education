class Ellipse:
    def __init__(self, *args):
        if args:
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]

    def __bool__(self):
        return all(map(lambda x: x in self.__dict__, ("x1", "y1", "x2", "y2")))

    def get_coords(self):
        if bool(self):
            return (self.x1, self.y1, self.x2, self.y2)
        raise AttributeError("нет координат для извлечения")


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]

for i in lst_geom:
    if i:
        i.get_coords()
