class Circle(object):
    def __init__(self, radius):
        """ Initializes self with radius """
        # your code here
        self.r = radius

    def get_radius(self):
        """ Returns the radius of self """
        # your code here
        return self.r
    def __add__(self, c):
        """ c is a Circle object 
        Returns a new Circle object whose radius is 
        the sum of self and c's radius """
        # your code here
        new_r = self.r + c.r
        return Circle(new_r)
    def __str__(self):
        """ A Circle's string representation is the radius """
        # your code here
        return f'Circle With A Radius Of {self.r}'


c1 = Circle(6)
c2 = Circle(5)
print(c1.get_radius())
print(c2.get_radius())
print(c1.__add__(c2))
print(c1)
print(c2)