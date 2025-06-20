def all_true(n, Lf):
    """ n is an int
        Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called 
    with n as a parameter. Otherwise returns False. 
    """
    # Your code here
    for i in Lf:
        if i(n) != True:
            return False
    return True

# Examples:    
print(all_true(6, [lambda x: x % 2 == 0, lambda y : y > 0])) # prints True 
print(all_true(3, [lambda x: x % 2 == 0, lambda y : y > 0])) # prints False 