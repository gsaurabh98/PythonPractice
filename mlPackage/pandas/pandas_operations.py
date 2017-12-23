import numpy as np
import pandas as pd
from numpy import random

d = {'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']}
df = pd.DataFrame(d)
print (df)

#to get the unique values of col2
print (df['col2'].unique())

#to get the number of unique values
print (df['col2'].nunique())

#to egt the unique value counts
print (df['col2'].value_counts())

#apply method, to perform the operation on column values by passing functions in it.
print (df['col2'].apply(lambda x: x*2))

#drop the colum
print (df.drop('col2' , axis =1))

#to get the index
print (df.index)

#to get the columns
print (df.columns)

#to sort the values of columns
print (df.sort_values('col2'))

#to get the null values
print (df.isnull())

#to get the top rows
print (df.head(2))

data = {'A': 'foo foo foo bar bar bar'.split(),'B': 'one one two two one one'.split(),'C': 'x y x y x y'.split(),'D':[1,3,2,5,4,1]}
df = pd.DataFrame(data)
print (df)

#pivot table
print (df.pivot_table(values= 'D',index = ['A','B'], columns = 'C'))
print (df.pivot_table(values= 'D',index = ['A','B'], columns = 'C').dropna())
