from math import sqrt


class PathLines:  # для описания маршрутов, состоящих из линейных сегментов
    def __init__(self, *args):
        self.lines_list = []

        for i, lineTo in enumerate(args, start=len(self.lines_list)):
            setattr(self, f"line{i}", lineTo)
            self.lines_list.append(lineTo)

    def get_path(self):
        return self.lines_list

    def get_length(self):
        L = 0
        priv_x = 0
        priv_y = 0
        for i in self.lines_list:
            L += sqrt((i.x - priv_x) ** 2 + (i.y - priv_y) ** 2)
            priv_x, priv_y = i.x, i.y

        return L

    def add_line(self, line):
        att_num = len(self.lines_list) + 1
        setattr(self, f"line{att_num}", line)
        self.lines_list.append(line)


class LineTo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
