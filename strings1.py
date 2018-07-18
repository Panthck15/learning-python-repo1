str1=input('Please enter a string to find the occurances:')
str2=input('Please enter the string:')
count=0
for char in str2:
    if str1.lower()==char.lower():
        count+=1
print(str1)
print(count)

