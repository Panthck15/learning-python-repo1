x=1
total=0
while x<51:
    total+=x
    if total>100:
        print('The max value is 100')
        print(total)
        print(x)
        break
    x+=1