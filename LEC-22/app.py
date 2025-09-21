import time

def convert_to_km(m):
    return m * 1.609

def compund(invest, interest, n_months):
    total = 0
    for i in range(n_months):
        total = total * interest + invest
    return total

# L_N = [1]
# for N in range(7):
#     L_N.append(L_N[-1] * 10)
        
# for N in L_N:
#     t0 = time.perf_counter()
#     convert_to_km(N)
#     dt = time.perf_counter() - t0
#     print(f"Converting {N} to KiloMeters Took {dt}s")


# for N in L_N:
#     t1 = time.perf_counter()
#     compund(N, 1.05, 12)
#     dt = time.perf_counter() - t1
#     print(f"Calculating Compund Took {dt}s")


# a little more complex example to measure time complexity
def sum(L):
    total = 0.0
    for i in L:
        total += i
    return total

# L_N = [1]
# for N in range(8):
#     L_N.append(L_N[-1] * 10)

# for N in L_N:
#     L = list(range(N))
#     t2 = time.perf_counter()
#     s = sum(L)
#     dt = time.perf_counter() - t2
#     print(f"calculating sum for {len(L)} elements took {dt:2e}s")


# Measuring time of finding elemnt in a list 

# brute force
def is_in(L, e):
    for el in L:
        if el == e:
            return el
    return None


# binary search 
def binary_is_in(L, e):
    lo = 0
    hi = len(L)
    for i in L:
        mid = (lo + hi) // 2
        if mid == e:
            return mid
        elif mid > e:
            hi = mid
        else:
            lo = mid

L = [1, 2, 3, 4, 5, 6, 7]
print(binary_is_in(L, 4))
print(binary_is_in(L, 5))
print(binary_is_in(L, 9))