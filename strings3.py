my_str=input('Please enter a string:')
str_vowels='aeiou'
str_print=''
for vow in str_vowels:
    if my_str.find(vow)!=-1:
        my_str=my_str.replace(vow,'')

print(my_str)