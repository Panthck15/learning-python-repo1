import numpy as np 
def top_5_elements(nparry):
    sorted_arr = np.sort(nparry)
    return sorted_arr [-5:]

arr=np.arange(30)
top_5 = top_5_elements(arr)
print(top_5)