Fn = []



def fib(n):
    if len(Fn) == 0:
        Fn.append(0)
        Fn.append(1)
        Fn.append(1)
        print(1)
        print(1)
        return
    NewFn = (Fn[n - 1]) + (Fn[n - 2])
    Fn.append(NewFn)
    print(NewFn)

def check():
    try:
        if len(str(Fn[-1])) != 1000:
            return True
    except:
        return False

while check() or len(Fn) == 0:
    fib(len(Fn))

print("The first value of n in which the term contains 1000 digits is " + str(len(Fn)-1))