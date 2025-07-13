# LIST COMPREHENSIONS

L = [1, 2, 3]
newL = [e ** 2 for e in L]
# print(newL)

# print([e for e in range(8 + 1) if e%2==0])

#print([len(x) for x in ['xy', 'abc', 7, '4.0'] if type(x) == str]) # if x in the inner list string put it's length in the list


# Intro To closures

def make_prod(a):
    def g(b):
        return a*b
    return g
val = make_prod(2)(3)
# print(val)


# Testing and Debugging 

# the concept of glass box testing 

#this code is from the lecture 

def abs(x):
    if x < 0:
        return -x
    else:
        return x

# print(abs(-1)) # 1
# print(abs(0)) # 0
# print(abs(-3)) # 3
# print(abs(3)) # 3


def is_pal(x):
    temp = list(x)
    temp.reverse()
    pal_word = ''.join(temp)
    print(pal_word, x)
    if pal_word == x:
        return True
    else: 
        return False


print(is_pal("ab")) # False
print(is_pal("rotator")) # True 