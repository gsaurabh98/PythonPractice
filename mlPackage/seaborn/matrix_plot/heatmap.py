import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

# print tips.head()
# print flights.head()

#to build the heatmap data should be in matrix form. beacuse index name should be match with the column value.
# corr method : co-relation will occur on number columns automatically.
tp = tips.corr()
print (tp)
# heatmap colors the cell values based on the gradients.
# it will set the cell numbers to the gradients and fill color accordingly
# we can pass one more argument annotations: annot = True to display the cell values
# cmap(color mapping) argument we use for coloring
sns.heatmap(tp, annot=True, cmap='Set1')
plt.show()

# tpt= tips.pivot_table(index = 'size',columns='sex',values='total_bill')
#
# print tpt
#
# sns.heatmap(tpt)
# plt.show()

# pivot_table we use it to build the matrix plot, which takes the argument index,columns and values.
fp = flights.pivot_table(index ='month', columns='year',values='passengers')

sns.heatmap(fp,linecolor='white',linewidths='0.6')
plt.show()