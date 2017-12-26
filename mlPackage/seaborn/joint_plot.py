import matplotlib.pyplot as plt
import seaborn as sns

dataset = sns.load_dataset('tips')

#takes x,y as an argument and it is bivariant means takes two variable.
#it basically compares two columns and builds the scatter plot.
#it takes one more argument called kind which refers to 'hex'(hexagon),'reg'(linear regression) etc.
sns.jointplot(x='total_bill',y='tip',data = dataset, kind = 'kde')
plt.show() 