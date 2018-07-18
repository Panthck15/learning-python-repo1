my_str=input('Please eneter a string:')
my_str_cap=''
x = input('Please enter a string: ')
y = ''
upper = False
for i in x:    
    if upper == False:        
        y += i.lower()        
        upper = True    
    else:        
        y += i.upper()        
        upper = False
print(y)
