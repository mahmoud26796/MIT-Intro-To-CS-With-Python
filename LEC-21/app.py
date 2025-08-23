import time
def c_to_f(c):
    counter = 3
    return (counter, c * 9.0 / 5 + 32)

def mysum(n):
    total = 0
    counter = 1
    for i in range(n):
        counter += 3
        total += 1
    return (counter, total)

def sqsum(n):
    total = 0
    counter = 1
    for i in range(n):
        counter += 1
        for j in range(n):
            counter += 3
            total += 1
    return (counter, total)


# tstart1 = time.time()
# print(c_to_f(10))
# dt1 = time.time() - tstart1
# print(dt1, "sec")


# tstart2 = time.time()
# print(mysum(5))
# dt2 = time.time() - tstart2
# print(dt2, "sec")


# tstart3 = time.time()
# print(sqsum(5))
# dt3 = time.time() - tstart3
# print(dt3, "sec")


# implementig time wrapper function  (Calculating Seconds)
# def time_wrapper(f, L):
#     print("Timing...", f.__name__)
#     for i in L:
#         print(f(i)[0])
#         tstart = time.time()
#         f(i)
#         dt = time.time() - tstart
#         # print(f"Calculating with {i} Took {dt} sec")
#     return "Done"

# implementig time wrapper function  (Calculating Operations)
def time_wrapper(f, L):
    print("Timing...", f.__name__)
    for i in L:
        counter = f(i)[0]
        if i == min(L):
            multiplier = 1.0
        else:
            multiplier = counter / float(prev)
        prev = counter
        print(f"Calculating with {i} Took {counter} ops, {multiplier} x more")
    return "Done"

L = [1, 10, 100, 1000, 10000, 1000000]

print(time_wrapper(c_to_f, L))