class Coordinates(object):
    def __init__(self, x_val, y_val):
        self.x = x_val
        self.y = y_val
    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5 


x = Coordinates(3, 4)
orig = Coordinates(0, 0)

print(x.distance(orig))
print(Coordinates.distance(x, orig))
print(type(x))
print(type(orig))