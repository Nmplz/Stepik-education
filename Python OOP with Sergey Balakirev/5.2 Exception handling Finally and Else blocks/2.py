class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y


a, b = input().split()

try:
    pt = Point(int(a), int(b))
except:
    pt = Point()
finally:
    print(f"Point: x = {pt._x}, y = {pt._y}")
