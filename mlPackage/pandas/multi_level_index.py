import pandas as pd
from numpy import random

#index levels

outside = 'G1 G1 G1 G2 G2 G2'.split()
print outside

inside = [1,2,3,1,2,3]
print inside

heir_index = list(zip(outside,inside))
print heir_index
new_heir_index = pd.MultiIndex.from_tuples(heir_index)
print new_heir_index

df = pd.DataFrame(random.randn(6,2),new_heir_index,['A','B'])
print df

# setting name to the index
df.index.names = ['Groups','Num']
print df.index.names

print df.loc['G1'].loc[[1,2]].loc[2].loc['A']
#or
print df.loc['G1'].loc[2]['A']


#cross section

print df.xs('G1')
print df.xs(1,level='Num')