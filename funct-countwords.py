def get_wordscount():
    my_str=input('Please eneter a string : ')
    my_list=my_str.split(' ')
    #print(len(my_list))
    return (len(my_list))

x=get_wordscount()
print(x)