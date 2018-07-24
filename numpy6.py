import numpy as np 

def one_dim_rand_arr(num1,num_rows,num_cols):
    np_arr=np.array(np.random.random(num1))
    return np_arr.reshape(num_rows,num_cols)


arr1=one_dim_rand_arr(6,2,3)
print(arr1)