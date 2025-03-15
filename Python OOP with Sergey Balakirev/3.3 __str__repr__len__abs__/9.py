class PolyLine:

    def __init__(self, start_coord, *args):
        self.start_coord = start_coord
        self.coords = []

        self.coords.append(start_coord)
        for i in args:
            self.coords.append(i)

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx):
        for i, v in enumerate(self.coords):
            if i == indx:
                self.coords.remove(self.coords[i])
                break

    def get_coords(self):
        return [x for x in self.coords]
