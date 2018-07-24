import pandas as pd 
import numpy as np 
df_wine_red=pd.read_csv('H:\DE\dsi-python-fundamentals\week6\day11-numpy_pandas\data\winequality-red.csv', delimiter=';')

s = pd.Series(df_wine_red.columns, dtype="category")

'''
#rows and columns
print(df_wine_red.shape)

#Data Types
print(df_wine_red.dtypes)

#Categories
print(s)


#count of Nan values
print(df_wine_red.count())
'''
#•What are the min, mean, max, median for all numeric columns?
print(df_wine_red.describe(include=[np.number]))