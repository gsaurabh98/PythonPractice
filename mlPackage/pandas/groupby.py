import numpy as np
import pandas as pd

data = {'Company': ['Google','Google','Apple','Apple','FB','FB'],
        'Person':['Charles','John','Peter','Andriana','Amy','Sarah'],
        'Sale':[200,150,170,210,300,240]}
df = pd.DataFrame(data)

print df

# we can use it by storing in variable
bycomp = df.groupby('Company')

print bycomp.count()
print bycomp.sum()
print bycomp.mean().loc['Google']
print bycomp.describe()
print bycomp.describe().transpose()['FB']