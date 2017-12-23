import pandas as pd

#Joining is a convenient method for combining.
# the columns of two potentially differently-indexed DataFrames into a single result DataFrame.

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2'])

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])


# by default it takes left join
print left.join(right)
#inner
print left.join(right,how='inner')
#left
print left.join(right,how='left')
#right
print left.join(right,how='right')
#outer
print left.join(right,how='outer')