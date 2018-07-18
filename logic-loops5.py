my_list=list(range(1,100))
i=0
while (i<len(my_list)):
    if (my_list[i]%5==0) and (my_list[i]%3==0):
        my_list[i]='FizzBuzz'
    elif my_list[i]%3==0:
        my_list[i]='Fizz'
    elif my_list[i]%5==0:
        my_list[i]='Buzz' 
    else:
        print(my_list)
