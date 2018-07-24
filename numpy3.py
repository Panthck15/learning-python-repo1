import numpy as np 
def shape_arr(num_rows,num_cols,num_fillvalue):
    num_arr=np.empty((num_rows,num_cols))
    num_arr.fill(num_fillvalue)
    return  num_arr


shape_arr1=shape_arr(4,4,17)
print(shape_arr1)
