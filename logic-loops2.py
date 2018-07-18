x=int(input('Please enter a number:')) 
if x%2==0: 
    print('Even Number') 
    if x%3==0: 
        print('Even and divisible by 3') 
elif x%2!=0 and x%3==0: 
    print('Odd and divisible by 3') 
else: 
    print('Odd Number')