import pandas as pd 
#data_list = [{'a':1,'b':2,'c':3},{'a':4,'b':5,'c':6,'d':7}]
#data_list = [{'a':1},{'b':5},{'c':3}]
#data_vals=[[1,2,3],[4,5,6]]
#data_cols=['a','b','c']
data_vals=[[1,2],[4,5,6]]
data_cols=['a','b','c']
#df=pd.DataFrame(data_list)
df=pd.DataFrame(data=data_vals,columns=data_cols)
print(df)