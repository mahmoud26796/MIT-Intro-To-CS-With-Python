#Functions
def div_by(n, d):
    return n % d == 0

print(div_by(10, 3)) # function calls replaced in memory with the returned value from the function
print(div_by(195, 13)) # so those lines in memory the first is False and the second is True 


# sum of odds between two nums
def sum_odds(a, b):
    result = 0
    for i in range(a, b + 1):
        result += 2 * i - 1
    return result



print(sum_odds(3, 5))