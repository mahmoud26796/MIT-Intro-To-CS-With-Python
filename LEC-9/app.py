
# print((lambda x: x % 2 == 0)(10))


def do_twice(n, fn):
    return fn(fn(n))


# print(do_twice(3, lambda x: x**2)) # returns 81


# TUPLES 

# SYNTAX    tuple = (1, 2, 3) can hold any data type/s together 

# sequence = (2, 'a', 4, (1, 2), True)
# print(sequence[0])
# print(sequence[1])
# print(sequence[2])
# print(sequence[3])
# print(sequence[4])
# print('########')
# print(sequence[3][0])

# we can of course loop over Tuples 

def char_counts(s):
    vowels = 'aeiou'
    v_counter = 0
    c_counter = 0
    for i in s:
        if i in vowels:
            v_counter += 1
        else:
            c_counter += 1
    
    return (v_counter, c_counter)


# print(char_counts('Sara'))


def sum_prod(L):
    sum = 0
    prod = 1
    for i in L:
        sum += i
        prod *= i

    return (sum, prod)


# print(sum_prod([1, 2, 3, 4, 5]))