
class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __hash__(self):
        return hash((self.width, self.height))

    def __eq__(self, other):
        return hash(self) == hash(other)
    



