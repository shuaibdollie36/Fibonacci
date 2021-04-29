
#Define a function using recursion that returns first 20
def fib(a):
    if a <= 1:
        return a
    else:
        return fib(a - 1) + fib(a - 2)


#Display Value
for i in range(20):
    print(str(fib(i)), end=" ")
