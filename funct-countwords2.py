def get_wordscount(my_str,str_seperator=' '):
    my_list=my_str.split(str_seperator)
    return (len(my_list))

x=get_wordscount(input('Please enter a string : '),input('Please enter a seperator : '))
print(x)