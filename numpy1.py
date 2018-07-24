import numpy as np 
def normalize1(arr):
    norm = np.linalg.norm(arr)
    if norm == 0: 
       return arr
    return arr / norm

def normalize2(arr):
    mean1=np.mean(arr)
    std1=np.std(arr)
    return arr -(mean1/std1)


np_array = np.array([1,2,3,4,5])
norm_arr=normalize1(np_array)
print(norm_arr)

np_array = np.array([1,2,3,4,5])
norm_arr=normalize2(np_array)
print(norm_arr)
