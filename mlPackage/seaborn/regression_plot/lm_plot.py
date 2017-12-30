import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
tips.head()

# here lmplot refers to linear model plot. x and y should be numerical column
# we can add another argument called:
#sns.lmplot(x = 'total_bill', y = 'tip',data=tips, hue = 'sex')

# we can add more functionality to the lmplot i.e. matlplotlib arguments.
# under the hood seaborn is calling matplotlib
# marker or scatter_kws (for marker size) as dictionary: s for size

# sns.lmplot(x = 'total_bill', y = 'tip',data=tips, hue = 'sex', markers=['o','*'],
#            scatter_kws= {'s':100})

# we can separate it using grid instead of hue. col argument will build the another plot based on category.
# we use this in row as well for another column.
# this will be done using facetgrid automatically, we dont need to call it explicitly.
# we can use hue argument as well to categorize the plot.
# Aspect and Size:Seaborn figures can have their size and aspect ratio adjusted with the size
# and aspect parameters for the plot.
sns.lmplot(x = 'total_bill', y = 'tip',data=tips,col='sex', row = 'time', hue = 'day',aspect=0.8,size =9)
plt.show()
