import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

#joint grid are genral version of the jointplot
# we need to pass the x and y parameter to build the graph against.
g = sns.JointGrid(x='total_bill',y ='tip',data=tips)

# we need to pass to plots arugment
g.plot(sns.regplot, sns.distplot)
plt.show()