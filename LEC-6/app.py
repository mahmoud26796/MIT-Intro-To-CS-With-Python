# FAST SQRT of a number with the Bisection search Algorithm


# x = 54321
# epsilon = 0.01
# num_guesses = 0
# low = 0.0
# high = x*1.5
# guess = (low + high) / 2.0

# while abs(guess**2 - x) >= epsilon:
#     if guess ** 2 < x:
#         low = guess
#     else:
#         high = guess
#     guess = (low + high) / 2.0
#     num_guesses+=1
# print(f'num guesses = {num_guesses}')
# print(f'{guess} is close enough to the sqrt of {x}')


# find cube with bisection search algorithm (with the else if statment approach that was in lecture)

cube = 0.5
epsilon = 0.01
if cube < 1:
    low = cube
    high = 1
else:
    low = 0
    high = cube
num_gusses = 0
guess = (low + high) / 2.0
while abs(guess ** 3 - cube) >= epsilon:
    if guess ** 3 < cube:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2.0
    num_gusses += 1
print(f'num gusses is {num_gusses}')
print(f'{guess} is close enogh to cube root of {cube}')