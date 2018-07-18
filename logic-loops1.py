x=int(input('Please enter a number:'))
if x<9:
    print('This is a good number')
elif x>9 and x<100:
    print('This is a better number')  
    if x%2==0:
        print('This is the best number')
else:
    print('This is a horrible number')