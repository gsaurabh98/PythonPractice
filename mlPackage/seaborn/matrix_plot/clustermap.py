import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

# cluster map will build the graph baserd on clustering,
#means similar groups are close to each other.
# we can put one more argument called: standard_scale = 1, means scaling will go till 1.
# tp = tips.corr()
# print tp
# sns.clustermap(tp, cmap='coolwarm')
# plt.show()

fp = flights.pivot_table(index ='month', columns='year',values='passengers')
sns.clustermap(fp,cmap = 'coolwarm',standard_scale=1)
plt.show()

