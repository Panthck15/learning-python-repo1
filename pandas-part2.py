import pandas as pd 
import numpy as np 
df_wine_red=pd.read_csv('H:\DE\dsi-python-fundamentals\week6\day11-numpy_pandas\data\winequality-red.csv', delimiter=';')

'''
#1.Grab the first 10 rows of the chlorides column. 
print(df_wine_red.iloc[0:10]['chlorides'])

#2.Grab the last 10 rows of the chlorides column. 
df_last_10rows = df_wine_red.tail(10)
print(df_last_10rows[0:10]['chlorides'])


#3.Grab indices 264-282 of the chlorides and density columns.
print(df_wine_red.loc[264:282,'chlorides':'density'])

#4.Grab all rows where the chlorides value is less than 0.10.
print(df_wine_red.query('chlorides<0.10'))

#5.Now grab all the rows where the chlorides value is greater than the column's mean (try not to use a hard-coded value for the mean, but instead a method).
print(df_wine_red[df_wine_red['chlorides'] > df_wine_red.loc[:,"chlorides"].mean()])

#6.Grab all those rows where the pH is greater than 3.0 and less than 3.5. 
print(df_wine_red.query('pH>3.0 and pH<3.5'))
#print(df_wine_red.head())
'''
#7.Further filter the results from 6 to grab only those rows that have a residual sugar less than 2.0.
print(df_wine_red.query('pH>3.0 and pH<3.5')['residual sugar']<2)
