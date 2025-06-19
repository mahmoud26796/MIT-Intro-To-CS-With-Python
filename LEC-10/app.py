"""
    write a function takes a positive integer n and return all numbers from 0 to n in order
"""
def make_orderd_list(n):
    L = []
    for i in range(n + 1):
        L.append(i)
    return L



# print(make_orderd_list(10))


"""
    write a function that takes a string s and returns how many words in it 
"""
def count_words(s):
    new_s = s.split(' ')
    return len(new_s)

# print(count_words("Helo it's Me"))

"""
 write a function that does the same as the function above it (count_words) 
 but return a list with the words sorted in aplhabet order
"""
def sort_words(sen):
     list_of_sen = sorted(sen.split(' '))
    #  lecture's first approach
    #  list_of_sen = sen.split(' ')
    #  list_of_sen.sort() 
     return list_of_sen 

# print(sort_words("Look At The Photograph"))


"""
 Let's Write A Function That Mutate The Inputs
"""
def squares(L):
    for i, e in enumerate(L):
         L[i] = e**2
    return L

print(squares([2, 3, 4]))