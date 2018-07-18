def get_factorial(n=10):
    ret_factorial=1
    for i in range(1,n):
        ret_factorial*=i
    return ret_factorial

x=get_factorial(7)
print(x)