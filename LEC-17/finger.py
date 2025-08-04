class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        # your code here
        self.r = radius
    def get_radius(self):
        """ Returns the radius of self """
        # your code here
        return self.r
    def set_radius(self, radius):
        """ radius is a number
        Changes the radius of self to radius """
        # your code here
        self.r = radius
    def get_area(self):
        """ Returns the area of self using pi = 3.14 """
        # your code here
        return 3.14 * (self.r ** 2) 
    def equal(self, c):
        """ c is a Circle object
        Returns True if self and c have the same radius value """
        # your code here

    def bigger(self, c):
        """ c is a Circle object
        Returns self or c, the Circle object with the bigger radius """
        # your code here
        return c.r * 2



c = Circle(6)
c2 = Circle(0)
Circle.set_radius(c2, 5)
print(c.get_radius())
print(c2.get_radius())
print(c.get_area())
print(c2.get_area())
print(c.bigger(c2))
print(c2.bigger(c))