class Box:
    def __init__(self):
        self.box = []

    def add_thing(self, obj):
        if isinstance(obj, Thing):
            self.box.append(obj)

    def get_things(self):
        return self.box

    def __eq__(self, other):
        box1 = self.box[:]
        box2 = other.box[:]
        for i in box1:
            if i in box2:
                box2.remove(i)
            else:
                break
        else:
            return True
        return False


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass
