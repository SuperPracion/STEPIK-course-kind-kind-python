class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.tracks = []

    def add_track(self, tr):
        self.tracks.append(tr)

    def get_tracks(self):
        return tuple(self.tracks)

    def __len__(self):
        len_1 = ((self.start_x - self.tracks[0].to_x) ** 2 + (self.start_y - self.tracks[0].to_y) ** 2) ** 0.5
        return int(len_1 + sum(self.get_length(i) for i in range(1, len(self.tracks))))

    def get_length(self, value):
        return ((self.tracks[value - 1].to_x - self.tracks[value].to_x) ** 2 + (self.tracks[value - 1].to_y - self.tracks[value].to_y) ** 2) ** 0.5

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


track1 = Track(0, 0)
track2 = Track(0, 1)

track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track1 == track2
