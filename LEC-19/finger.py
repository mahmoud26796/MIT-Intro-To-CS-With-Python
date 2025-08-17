class Container(object):
    """
    A container object is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initializes an empty list
        """
        self.myList = []

    def size(self):
        """
        Returns the length of the container list
        """
        # Your code here
        return len(self.myList)
    def add(self, elem):
        """
        Adds the elem to one end of the container list, keeping the end
        you add to consistent. Does not return anything
        """
        # Your code here
        self.myList.append(elem)
class Stack(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The newest element in the container list is removed
        Returns the element removed or None if the queue contains no elements
        """
        # Your code here
        if self.size():
            elem = self.myList.pop()
            return elem
        return None
    


c1 = Container()
s1 = Stack()
print(c1.size())
c1.add(1)
c1.add(2)
c1.add(3)
print(c1.size())

print(s1.size())
s1.add(1)
s1.add(2)
s1.add(3)
print('S Len => ', s1.size())
print(s1.remove())
print('S Len => ', s1.size())