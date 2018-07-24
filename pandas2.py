import pandas as pd 
#Read a csv file
#df=pd.read_csv('winequality-red.csv', delimiter=';')
#df=pd.read_csv('H:/DE/dsi-python-fundamentals/week6/day11-numpy_pandas/data/winequality-red.csv', delimiter=';')
df=pd.read_csv('H:\DE\dsi-python-fundamentals\week6\day11-numpy_pandas\data\winequality-red.csv', delimiter=';')
#print(df)
#print(df.shape)
#print(df.info)
#print(df.head(10))
#print(df.tail(10))
#print(df['chlorides'])  #Column Name
df2=df.copy()
cols=df2.columns.tolist()
cols=[col.replace(' ','_') for col in cols]
print(cols)
#df3=df2[['chlorides','volatile_acidity']]
#print(df3.head)
#print(df2.iloc[0:10])
#print(df2.head())
#print(df2[df2['chlorides'] <= 0.08])
#print(df2[(df2['chlorides'] <= 0.08]) & (df2['chlorides'] >=0.04)])
#print(df.query('chlorides >=0.04 and chlorides <=0.08'))
#print(df2.quality.unique())
wine_df=df2.copy()
#print(wine_df.head())
groupby_obj=wine_df.groupby('quality')
#print(groupby_obj.mean())
#print(groupby_obj.min())
#print(groupby_obj.max())

#groupby_obj.count()['quality']
#print(wine_df.sort_values('quality',ascending=True))
#print(wine_df.sort_values(['quality','alcohol'], ascending=[False,True]))
print(wine_df.head())
df['non_free_sulfur_dioxide']=wine_df['total sulfur dioxide']-wine_df['free sulfur dioxide']
wine_df.drop('zeros',axis=1,inplace=True)

wine_df2=wine_df.copy()
wine_df2.evel('non_sulfur_diaxide=total sulfur dioxide-free sulfur dioxide', inplace=True)
print(wine_df2.head())
wine_df2.dropna(inplace=True)
df2 = df.copy()
df2.rename(columns={'total sulfur dioxide':'total_sulfur_dioxide','free sufer dioxide':'free_sufer_dioxide'})