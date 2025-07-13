def count_sqrts(nums_list):
    """
    nums_list: a list
    Assumes that nums_list only contains positive numbers and that there are no duplicates.
    Returns how many elements in nums_list are exact squares of elements in the same list, including itself.
    """
    # Your code here
    sqr_list = [e for e in nums_list if e**2 in nums_list]
    return len(sqr_list)
# Examples:    
print(count_sqrts([3,4,2,1,9,25])) # prints 3