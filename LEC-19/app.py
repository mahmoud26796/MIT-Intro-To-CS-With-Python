# def make_animals(L1, L2):
#     L3 = []
#     for i in range(len(L2)):
#          L3.append({L1[i]: L2[i]})
#     return L3


# L1 = [1, 2, 3]
# L2 = ["blobfish", "crazyant", "parafox"]

# print(make_animals(L1, L2))


class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_animals(L1, L2):
        L3 = []
        for i in range(len(L2)):
            L3.append(Animal(L2[i], L1[i]))
        return L3
    def __str__(self):
        return '{' + f'{self.name}: {self.age}' + '}'


# L1 = [1, 2, 3]
# L2 = ["blobfish", "crazyant", "parafox"]
# animals  = Animal.make_animals(L1, L2)
# for i in animals:
#     print(i)



class Cat(Animal):
    def __init__(self, age):
        self.age = age
    def __str__(self):
        return super().__str__()
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

class Person(Animal):
    def __str__(self):
        return super().__str__()
    def add_friends(L):
        pass


cat1 = Cat(3)
person1 = Person("Sara", 29)
cat1.set_name("Fluffy")
# write a function to map in a dict the name of the person to his cat

def make_pets(d):
    for k, v in d.items():
        if type(k) == Person and type(v) == Cat:
            return f'{k.name} - {v.get_name()}'
        return None

    

d = {person1: cat1}
print(make_pets(d))