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

print(count_words("Mahmoud Loves Sara Hany"))
print(count_words("Helo it's Me"))