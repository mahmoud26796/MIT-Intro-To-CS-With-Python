def sum_digits_except(s):
    total = 0
    for char in s:
        try:
            val = int(char)
            total += val
        except:
            print(f"Couldn't Convert {char}")
    return total


# print(sum_digits_except('123abc'))


# Handling Specific Exeption

def divide_nums():
    result = 0
    try:
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        if a > b:
            result = a/b
        elif b > a:
            result = b/a
    except ValueError:
        print("Could not convert to a number ")
    except ZeroDivisionError:
        print("Can not Divide By Zero!")
    except:
        print("Something went very wrong")
    return result

# print(divide_nums())


# Rasing custom error message 

def sum_digits_rais(s):
    assert len(s) != 0, 'Input Can not be Empty String'
    total = 0
    for char in s:
        try:
            val = int(char)
            total += val
        except:
            raise ValueError("string Contained Values Cannot be Conberted to Int()")

    return total


# print(sum_digits_rais(''))

# pairwise division problem from lecture
def pairwise_div(Lnum, Ldenom):
        assert len(Lnum) == len(Ldenom), "Both Lists Has To Have Same Amount Of Numbers"
        res = []
        for i in range(len(Lnum)):
            try:
                # res = [Lnum[i] / Ldenom[i] for i in range(len(Lnum))] List Comprehension Solution
                # regular loop syntax solution :-
                res.append(Lnum[i] / Ldenom[i]) 
            except ZeroDivisionError:
                raise ZeroDivisionError("can't divide by zero!")
            except TypeError:
                raise TypeError("can't divide num by char or string")
            except:
                raise "Division Failed!"



        return res

L1 = [4, 5, 6]
L2 = [1, 's', 3]
print(pairwise_div(L1, L2))
