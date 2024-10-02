Fn = [0, 1]

inp = int(input("Enter how many digits you would like to find the first value of n for the respective term in the Fibonacci sequence to consist of that many digits: "))
print(0)


def fib(n):
    if len(Fn) == 2:    print(1)
    new_fn = (Fn[n - 1]) + (Fn[n - 2])
    Fn.append(new_fn)
    print(new_fn)


def check():
    try:
        if len(str(Fn[-1])) != inp:
            return True
    except:
        return False


while check() or len(Fn) == 0:
    fib(len(Fn))

print("The first value of n in which the term contains " + str(inp) + " digits is " + str(len(Fn) - 1))
