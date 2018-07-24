import numpy as np 
def normalize2(arr):
    mean1=np.mean(arr)
    std1=np.std(arr)
    return arr -(mean1/std1)

np_array = np.array([1,2,3,4]).reshape(2,2)
print(np_array)
norm_arr=normalize2(np_array)
print(norm_arr)
