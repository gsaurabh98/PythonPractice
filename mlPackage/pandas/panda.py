import numpy as np
import pandas as pd
from numpy import random

np.random.seed(101)
df = pd.DataFrame(random.randn(5,4),['A','B','C','D','E'],columns = ['w','x','y','z'])
print df

#comparison operator
#booldf = df >0
#print booldf

#print df[booldf]
#or
print df[df>0]

print df[df['w']>0]

#if we want to retrieve only column x value
print df[df['w']>0][['x','y']]

booldf = df['w']>0
result =  df[booldf]
mycols = ['x','y']
print result[mycols]

print df[(df['w']>0) & (df['x']<0)]

# reset the index

print df.reset_index()


newindex = 'CA NY WY OR CO'.split()
df['states'] = newindex
print df.set_index('states')
