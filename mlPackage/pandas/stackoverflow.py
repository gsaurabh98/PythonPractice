import pandas as pd
import numpy as np

data = {'x':[1,2,np.NaN,np.NaN]}
df = pd.DataFrame(data)
print (df)
def fil(val):
  for i in val:
    i+=1
print (df['x'].fillna().apply(lambda y: fil(y)))
