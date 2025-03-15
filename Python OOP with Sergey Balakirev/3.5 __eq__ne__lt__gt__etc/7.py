class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume
        self.indx = self.ro * self.volume

    def __eq__(self, other):
        if isinstance(other, Body):
            return self.indx == other.indx
        return self.indx == other

    def __le__(self, other):
        if isinstance(other, Body):
            return self.indx < other.indx
        return self.indx < other

    def __lt__(self, other):
        if isinstance(other, Body):
            return self.indx <= other.indx
        return self.indx <= other
