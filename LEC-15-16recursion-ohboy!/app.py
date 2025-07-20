from datetime import datetime
# recursive multiplication
def mult_recursive(a, b):
    if b <= 1:
         return a
    return a + mult_recursive(a, b - 1)


# print(mult_recursive(5, 9))


# recursive power 
def power_recursive(n, p):
    if p == 1:
        return n
    if p == 0:
        return 1
    return n* power_recursive(n, p-1)
# print(power_recursive(2, 3))


# fibonacci sequence 
def fib(n):
    start = datetime.now()
    if n <= 2:
         return 1
    

    ans = fib(n-1) + fib(n-2)
    end = datetime.now()
    time = end - start
    print(time)
    return ans

# print(fib(7))

# the concept of memoization to improve the algorithm performance
# note fib sequence without this approach will have a big O notation of (2^n)
# big O later in the course at this point but its bad
def fib_eff(n, d):
    start = datetime.now()
    if n in d:
        return d[n]
    ans = fib_eff(n-1, d) + fib_eff(n-2, d)
    d[n] = ans 
    end = datetime.now()
    time = end - start
    print(time)
    return ans


d = {1:1, 2:1}
# print(fib_eff(7, d))


def score_count(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3: 
        return 3
    return score_count(x-1) + score_count(x-2) + score_count(x-3)


# print(score_count(25))


# total recursion (summing elements in a list recursivly) => from lecture
def total_recur(L):
    if len(L) == 1:
        return L[0]
    return L[0] + total_recur(L[1:])

L = [30, 40, 50]
# print(total_recur(L))

#is elemnt in the list ? 
def in_list(L, e):
    if len(L) == 1:
        return L[0] == e
    elif L[0] == e:
        return True
    return in_list(L[1:], e)

# print(in_list(L, 50)) #TRue
# print(in_list(L, 40)) #True
# print(in_list(L, 70)) #False


# Flatten a List of lists 
def flatten(L):
    if len(L) == 1:
        return L[0]
    return L[0] + flatten(L[1:])

# print(flatten([[1, 2, 3], [4, 5, 6]])) # => [1, 2, 3, 4, 5, 6]


def in_list_of_lists(L, e):
    myL = flatten(L)
    return in_list(myL, e)

# print(in_list_of_lists([[1, 2], [3, 4], [5, 6, 7]], 3)) # => True


def reverse_list(L):
    if len(L) == 1:
        return L
    return reverse_list(L[1:]) +  [L[0]]

# print(reverse_list([1, 2, 3, 4]))


def deep_reverse(L):
    if len(L) == 1:
        if type(L[0]) != list:
            return L
        else:
            return [deep_reverse(L[0])]
    else:
        if type(L[0]) != list:
            return deep_reverse(L[1:]) + [L[0]]
        else:
            return deep_reverse(L[1:]) + [deep_reverse(L[0])]
print(deep_reverse([[1, 2], 3, 4, [5, 6], [7, 8]]))