class Track:
    def __init__(self, start_x=0, start_y=0):
        self.x = start_x
        self.y = start_y
        self._tracks = []

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __len__(self):
        x1, y1 = self.x, self.y
        s = 0
        for obj in self._tracks:
            x2, y2 = obj.to_x, obj.to_y
            s += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            x1, y1 = x2, y2
        return int(s)

    def add_track(self, tr):
        self._tracks.append(tr)

    def get_tracks(self):
        return tuple(self._tracks)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
