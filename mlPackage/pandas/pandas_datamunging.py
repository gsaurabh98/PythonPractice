import numpy as np
import pandas as pd
from numpy import random

d = {'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz'],'col4': [22,3,1,2]}
df = pd.DataFrame(d)
#print (df)

#to read data from csv file
#print (pd.read_csv('C:\\Users\\saurabh.v.sharma\\Downloads\\dataframe.csv', index = False))

#to convert the dataframe into csv file
#data_csv = df.to_csv('C:\\Users\\saurabh.v.sharma\\Downloads\\dataframe.csv' )
#print (data_csv)

#to read from the excel file
#print (pd.read_excel('C:\\Users\\saurabh.v.sharma\\Downloads\\dataframe.csv', index = False, sheetname = 'Sheet1'))

#to convert the dataframe into excel file
#data_excel = df.to_excel('C:\\Users\\saurabh.v.sharma\\Downloads\\dataframe.xlsx', sheet_name = 'NewSheet' )
#print (data_excel)

#to read from the HTML
# read_data_html = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
# print (read_data_html.head())

#to convert the dataframe into excel file
#data_html = df.to_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
#print (data_html)

#to convert data into sql
from sqlalchemy import create_engine
#to create sql engine in memory
engine = create_engine('sqlite:///:memory:')
df.to_sql('table_name',engine, index = False)

#to read the data from sql
data_sql = pd.read_sql('table_name',con =engine)
print (data_sql)