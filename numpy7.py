import numpy as np 

def one_dim_rand_arr(num_arr,num_ch):
    sel_lst=[]
    for i in range(num_ch):
        sel_ch=np.random.choice(num_arr)
        sel_lst.append(sel_ch)
    return sel_lst


arr1=np.array([1,2,3,4,5,6,7,8])
print(one_dim_rand_arr(arr1,3))