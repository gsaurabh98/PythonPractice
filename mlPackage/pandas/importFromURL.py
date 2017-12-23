import pandas as pd

#ufo is a variable to store the URL CSV data
ufo = pd.read_table('http://bit.ly/uforeports', sep = ',')

# head will show the top values. head(5)-> 5 values
#print ufo.head()

# it will show the index and state values
#print ufo.State

# concatenation of two columns City and state into new column 'Location'
ufo['Location'] = ufo.City +', '+ ufo.State

#print ufo.head()

# shape will show the rows and columns (rows,columns)
#print ufo.shape

# dtypes will show the datatypes
#print ufo.dtypes

# columns will show the heading or column names
#print ufo.columns

#sort_values will sort based of values given in list, ascending = False means descending
#print ufo.sort_values(['City','State'],ascending=False).head(10)

#drop will remove the column name
# axis = 1 and axis = 0 means x axis and y axis repectively
# inplace = True means it doesn't return a copy of an object.
#ufo.drop(['Colors Reported','Location'],axis=1,inplace=True)
#print ufo

# we can sort the values bases on specific columns. like: variable.column_name.sort_values
print ufo.State.sort_values()