import pandas as pd

left1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

print pd.merge(left1,right1)
#or
print pd.merge(left1,right1, how='inner',on = 'key')

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

# by default it takes inner join
print pd.merge(left,right , how = 'inner', on= ['key1','key2'])
# outer join
print pd.merge(left,right , how = 'outer', on= ['key1','key2'])
# left join
print pd.merge(left,right , how = 'left', on= ['key1','key2'])
# right join
print pd.merge(left,right , how = 'right', on= ['key1','key2'])

