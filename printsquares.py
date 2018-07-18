my_list=input('Please enter numbers : ')
my_squares=[int(num)**2 for num in my_list]
#print(my_squares)
#my_dict={int(num)**2 for num in my_list}
my_dict={}
for num in my_list:
    my_dict[num]=int(num)**2 
print(my_dict)