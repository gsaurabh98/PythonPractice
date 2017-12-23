import pandas as pd

dictionary_eg = { 'days': [1,2,3,4,5,6],'visitors': [1000,340,1200,600,200,580],'bounce_rate':[20,12,15,19,7,10]}


df = pd.DataFrame(dictionary_eg)

df.set_index('days', inplace= True) # if we dont put inplace it will keep the days keys as well

# rename keyword is use to change the column name in dataframe
df = df.rename(columns = {'visitors':'users'})

print (df)