import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
print titanic.head()

sns.set_style('whitegrid')

#Question1
# sns.jointplot(x ='fare', y ='age',data=titanic)
# plt.show()

#Question2
# sns.distplot(titanic['fare'],kde=False,color='red',bins=30)
# plt.show()

#Question3
# sns.boxplot(x='class',y='age',data=titanic,palette='rainbow')
# plt.show()

#Question4
# sns.swarmplot(x='class',y='age',data=titanic,palette='Set2')
# plt.show()

#Question5
# sns.countplot(x='sex',data=titanic)
# plt.show()

#Question6
# t_cor = titanic.corr()
# sns.heatmap(t_cor,cmap='coolwarm')
# plt.title('titanic.corr()')
# plt.show()

#Question7
g = sns.FacetGrid(data=titanic,col='sex')
g.map(plt.hist,'age')
plt.show()