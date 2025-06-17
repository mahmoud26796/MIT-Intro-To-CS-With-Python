# GUESS_AND_CHECK

# Basic Idea Givin an int => x we want to know if there is another int wich is the square root of x
# Start with a guess and check if it is the right answer


# 1 guess if x is a perfect square root

# guess = 0
# x = int(input("Please Enter an Integer "))

# while guess ** 2 < x:
    # guess = guess + 1
# if guess ** 2 == x:
    # print(f"{x} is a Perfect Square root with sqrt of {guess}")
# else:
    # print(f"{x} is not a perfect Square root")


# Secret Number Program (Found/ Not found)

# secret_num = 5
# found = False
# for i in range(10):
#     if i == secret_num:
#         print("Found!")
#         found = True
#         break

# if not found:   # ANOTHER APPROACH WOULD BE JUST DO AN ELSE STATMENT FOR THE FOR LOOP IT SELF (VALID IN PYTHON)
#     print("Not Found")



# guess and check positive an negative cupes

# cube = int(input("Enter Your Number: "))

# for guess in range(abs(cube) + 1):
#     if guess ** 3 == abs(cube):
#         if cube < 0:
#             guess = -guess
#         print(f"Cube root of {cube} is {guess}")
# Faster Version
# for guess in range(abs(cube) + 1):
#     if guess**3 >= abs(cube):
#         break

# if guess**3 != abs(cube):
#     print(f"{cube} is not a perfect Cube")
# else:
#     if cube < 0:
#         guess = -guess
#     print(f"Cube root of {cube} is {guess}")


# word peoblem (selling tickets) solution

# NAIVE 
# for alyssa in range(11):
#     for ben in range(11):
#         for cindy in range(11):
#             total = (alyssa + ben + cindy == 10)
#             two_less = (ben == alyssa - 2)
#             twice = (cindy == alyssa * 2)
#             if(total and two_less and twice):
#                  print(f"alyssa sold {alyssa}, ben sold {ben}, cindy sold {cindy}")
# #Better Mathimatical Solution WHY? because the previos one is cubic time complexity [Too Slow]
# print("################################")
# for alyssa in range(1001): # O(n) way better than O(n^3)
#     ben = max(alyssa - 20, 0)
#     cindy = alyssa * 2
#     if alyssa + ben + cindy == 1000:
#         print(f"alyssa sold {alyssa}, ben sold {ben}, cindy sold {cindy}")



# convert to binary and Handling negative inputs

num = int(input("Ener Your Number: "))
neg = False
if num < 0:
    neg = True
    num = abs(num)
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result

    num = num//2
if neg:
    print(f"-{result}")
else:
    print(result)