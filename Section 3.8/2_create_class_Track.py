class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.points = []

    def add_point(self, x, y, speed):
        self.points.append({'x': x, 'y': y, 'speed': speed})

    def __getitem__(self, item):
        try:
            x, y, speed = self.points[item].values()
            return (x, y), speed
        except:
            raise IndexError('некорректный индекс')

    def __setitem__(self, key, value):
        try:
            self.points[key]['speed'] = value
        except:
            raise IndexError('некорректный индекс')


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3] # IndexError
