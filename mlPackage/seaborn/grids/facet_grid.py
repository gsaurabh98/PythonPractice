import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
print tips.head()

# in FacetGrid we need to pass col and row argument to create the grid
g = sns.FacetGrid(tips, col= 'sex',row='smoker')
# below we are buliding distplot and passing argument 'total_bill' against which we need to plot.
# it will create the automatic labes based on columns and rows.
g.map(sns.distplot,'total_bill')

# we can build other plots as well and based on that we need to pass the arguments.
#g.map(plt.scatter,'tip','total_bill' )
plt.show()