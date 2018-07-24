import numpy as np 
def bottom_5_elements(nparry):
    sorted_arr = np.sort(nparry)
    return sorted_arr [5:]

arr=np.arange(30)
top_5 = bottom_5_elements(arr)
print(top_5)