import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[1,np.nan,np.nan],'C':[1,2,3],'D':[np.nan,np.nan,np.nan]}
df = pd.DataFrame(d)
print df

# for removing NaN value
print df.dropna()

#by removing column which has Nan
print df.dropna(axis=1)

#Keep only the rows with at least 2 non-na values:
print df.dropna(thresh=2)

#Drop the columns where all elements are nan:
print df.dropna(axis=1,how='all')

#filling the NaN Value
print df.fillna(value = 'Missing Value')

# filling value in particular column
print df['A'].fillna(value=df['A'].mean())