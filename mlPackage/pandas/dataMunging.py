import pandas as pd

#demand_sheet = pd.read_csv("C:\\Users\\Saurabh\\Downloads\\demand.xlsx",index_col= 0, error_bad_lines=False)

#demand_sheet.to_html('demand.html')

#df1 = pd.DataFrame({'HPI': [80,90,70,60],'Int_Rate': [2,1,2,3],'Ind_GDP':[50,45,60,20]},
                   #index=[2001,2002,2003,2004])

#df2 = pd.DataFrame({'HPI': [70,90,80,60],'Int_Rate': [3,1,5,3],'Ind_GDP':[30,45,60,20]},
                  # index=[2004,2006,2007,2008])

# concat will concatinate the two dataframes,
# if we have different key name it will add those keys and corresponding values

#df2.to_csv('df2.csv')
#concat_df = pd.concat([df1,df2])

file =  pd.read_csv('concat_df.csv',index_col= 0)
file.to_html('concat_df.xml',index= False)

print 'done'