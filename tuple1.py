my_str=input('Please enter some numbers : ')
str1=my_str[0::2]
str2=my_str[1::2]
#print(str1)
#print(str2)
print(list(tuple(zip(str1,str2))))