class Coordinate(object):
    def __init__(self, x_val, y_val):
        self.x = x_val
        self.y = y_val
    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5 


x = Coordinate(3, 4)
orig = Coordinate(0, 0)

# print(x.distance(orig))
# print(Coordinate.distance(x, orig))
# print(type(x))
# print(type(orig))


class Circle(object):
    def __init__(self, center, radius):
        if type(center) != Coordinate:
            raise ValueError
        if type(radius) != int:
            raise ValueError
        self.center = center
        self.radius = radius
    def is_inside(self, point):
        if type(point) != Coordinate:
            raise ValueError
        return point.distance(self.center) <= self.radius

center = Coordinate(3, 4)
c1 = Circle(center, 5)

# print(c1.center.x, c1.radius)

p = Coordinate(2, 5)
# print(c1.is_inside(p))


# our own fraction type 
class SimpleFraction(object):
    def __init__(self, n, d):
        self.num = n
        self.denom = d
    def plus(self, oth):
        top = self.num*oth.denom + self.denom*oth.num
        bottom = self.denom*oth.denom
        return top/bottom
    def __mul__(self, oth):
        top = self.num*oth.num
        bottom = self.denom*oth.denom
        return top/bottom
    def get_inverse(self):
        return self.denom/self.num
    def invert(self):
        temp = self.num
        self.num = self.denom
        self.denom = temp
    def __str__(self):
        return f'{self.num}/{self.denom}'
    def reduce(self):
        def gdc(n, d):
            while d != 0:
                (d, n) = (n%d, d)
            return n
        if self.denom == 0:
            return None
        elif self.denom == 1:
            return SimpleFraction(self.num, 1)
        else:
            greates_common_divisor = gdc(self.num, self.denom)
            top = int(self.num / greates_common_divisor)
            bottom = int(self.denom / greates_common_divisor)
            return SimpleFraction(top, bottom)
# f = SimpleFraction(3,4)
# f2 = SimpleFraction(1, 2)
f3 = SimpleFraction(2,12)
# print(f.num, f.denom)
# print(f)
# print(f.times(f2))
# print(f.plus(f2))
# print(f.get_inverse())
# f.invert()
# print(f.num, f.denom)
# print(f)
# print(type(f))
# print(isinstance(f, SimpleFraction))
print(f3.reduce())
a = SimpleFraction(4, 1)
b = SimpleFraction(3, 9)
ar = a.reduce()
br = b.reduce()
print(ar, type(ar))
print(br, type(br))
c = ar * br
print(c)