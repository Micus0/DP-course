import copy


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Start: {self.start.x}, {self.start.y}. End: {self.end.x}, {self.end.y}"


l1 = Line(Point(1, 2), Point(5, 8))
l2 = l1.deep_copy()
l2.start.x = 5
l2.end.y = 10

print(l1, "\n", l2)
