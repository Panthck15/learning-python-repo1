def get_wordscount(my_str,str_seperator=' '):
    my_list=my_str.split(str_seperator)
    my_list2=[]
    for str1 in my_list:
        my_list2.append(len(str1))
    return (my_list2)

x=get_wordscount(input('Please enter a string : '),input('Please enter a seperator : '))
print(x)