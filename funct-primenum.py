def is_primenumber(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return (num,"is not a prime number")
        
            else:
                return(num,"is a prime number")
        
    else:
        return (num,"is not a prime number")

x=is_primenumber(5)
print(x)