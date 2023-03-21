class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

x, y = input().split()

try:
    point = Point(int(x), int(y))
except:
    try:
        point = Point(float(x), float(y))
    except:
        point = Point()
finally:
    print(f"Point: x = {point.x}, y = {point.y}")