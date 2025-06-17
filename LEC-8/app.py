def  is_trianguler(n):
    """
        n is and Integer > 0
        return True if n is triangular  i.e, equals a continued summation  of natrural numberx 
        like => (1+2+3....k), False Otherwise
    """
    total = 0
    for i in range(n + 1):
        total += i
        if total == n:
            # print(total)
            return True
    else:
        # print(total)
        return False

# print(is_trianguler(1))
# print(is_trianguler(2))
# print(is_trianguler(3))
# print(is_trianguler(4))
# print(is_trianguler(5))
# print(is_trianguler(6))

def bisection_root(x, epsilon):
    num_guesses = 0
    low = 0.0
    high = x
    guess = (low + high) / 2.0

    while abs(guess**2 - x) >= epsilon:
        if guess ** 2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
        num_guesses+=1
    # print(f'num guesses = {num_guesses}')
    # print(f'{guess} is close enough to the sqrt of {x}')
    return guess

# print(bisection_root(4, 0.01))
# print(bisection_root(123, 0.01))
# print(bisection_root(10, 0.1))

def count_nums_with_sqrt_close_to(n, epsilon):
    total = 0
    for i in range(n**3):
        res = bisection_root(i, epsilon)
        if abs(n - res) <= epsilon:
            total += 1
    return total


print(count_nums_with_sqrt_close_to(10, 0.1))