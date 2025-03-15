class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.track = []

    def __len__(self):
        return len(self.track)

    def add_point(self, x, y, speed):
        self.track.append([x, y, speed])

    def __getitem__(self, item):
        if not item < len(self):
            raise IndexError("некорректный индекс")
        a, b, c = self.track[item]
        return [(a, b), c]

    def __setitem__(self, key, value):
        if not key < len(self):
            raise IndexError("некорректный индекс")
        self.track[key][2] = value
