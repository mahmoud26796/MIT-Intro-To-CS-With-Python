"""
    L is a list mutate it to remove all elements in L that equals to the second parameter e 
    Returns None
"""

def remove_all(L, e): # first glance approach
    L_to_return = []
    for i in L:
        if i == e:
            continue
        else:
            L_to_return.append(i)
    print(L_to_return)

# print(remove_all([1, 2, 2, 2], 2))

"""
lecture approach is to make a copy of L right away like => Lnew = L[:] wich copy all elements of L in  Lnew and then iterate over Lnew 
""" 

#same problem but with remove built in function 
def our_remove(L, e):
    while e in L:
        L.remove(e)
    return L
print(our_remove([1, 2, 2, 2], 2))


