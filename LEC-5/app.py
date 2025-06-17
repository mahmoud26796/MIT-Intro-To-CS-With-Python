# x = 0
# for i in range(10):
#     x += 0.1
# print(x == 10) # False ! but WHY !!
# print(f'{x} == {0.1*10}') #0.999999999 not 1 ! WHY 


# fLOATING POINT ERRORS



# x = 0.625
# p = 0
# while ((2**p)*x) % 1 != 0:
#     print(f'reminder = {str((2**p)*x - int((2**p)*x))}') # finds the power of two so we can get the whole number out of it and then get it's binary representation
#     p += 1
# num = int((2**p)*x) # num is 5 in this case 
# result = ''
# if num == 0:
#     result = '0'
# while num > 0:
#     result = str(num%2) + result # getting the binray repres. of num wich is 5 in our case
#     num = num//2
# for i in range(p - len(result)):
#     result = '0' + result
# result = result[0: -p] + '.' + result[-p:] # putting a point in the result string and move it three spots to the left (-ve direction)

# print(f'The Binary Representation For The Decimal number {x} is {result}')

#######################################################################################

# Approximation Method Algorithm

# x = 36
# epsilon = 0.01
# num_guesses = 0
# guess = 0.0
# increment = 0.0001

# while abs(guess ** 2 - x) >= epsilon and guess ** 2 <= x: # the second condition to not over shoot the Epsilon with bigger numbers 
#     guess += increment
#     num_guesses += 1
# print(f"num guesses is {num_guesses}")
# print(f"{guess} is close enough to the sqrt of {x}")


