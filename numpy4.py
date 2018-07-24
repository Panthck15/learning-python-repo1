import numpy as np 
     
def math_operation(num_arr,math_opr,num1):
    if math_opr=='+':
        num_arr1=num_arr + num1
    elif math_opr=='-':
        num_arr1=num_arr - num1
    elif math_opr=='*':
        num_arr1=num_arr * num1
    elif math_opr=='/':
        num_arr1=num_arr / num1
    else:
        pass
   
    return num_arr1

num_arr2=np.array([1,2,3,4,5])
math_opr="*"
num_arr=math_operation(num_arr2 , math_opr , 5)
print(num_arr)
