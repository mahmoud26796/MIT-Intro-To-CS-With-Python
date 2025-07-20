# lecture 15 finger ex
def recur_power(base, exp):
    """
    base: int or float.
    exp: int >= 0

    Returns base to the power of exp using recursion.
    Hint: Base case is when exp = 0. Otherwise, in the recursive
    case you return base * base^(exp-1).
    """
    # Your code here  
    if exp == 0:
        return 1
    return base * recur_power(base, exp-1)
# Examples:
# print(recur_power(2,5))  # prints 32


# lecture 16 finger ex
def flatten(L):
    """ 
    L: a list 
    Returns a copy of L, which is a flattened version of L 
    """
    # Your code here  
    if len(L) == 1:
       if type(L[0]) != list:
          return L
       else:
        return flatten(L[0])
    else:
        if type(L[0]) != list:
            return [L[0]] + flatten(L[1:])
        else:
            return flatten(L[0]) + flatten(L[1:])
# Examples:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]