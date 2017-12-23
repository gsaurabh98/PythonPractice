
import pandas as pd

dictionary_eg = { 'days': [1,2,3,4,5,6],'visitors': [1000,340,1200,600,200,580],'bounce_rate':[20,12,15,19,7,10]}

df = pd.DataFrame(dictionary_eg) # to covert the value into kind of table

#df.head(args) means printing first agrs value
print (df.head(2))


#df.tail(args) means printing first agrs value
print (df.tail(2))
