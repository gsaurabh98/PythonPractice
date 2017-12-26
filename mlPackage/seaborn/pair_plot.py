import matplotlib.pyplot as plt
import seaborn as sns

dataset = sns.load_dataset('tips')

print dataset.head()

#refers to a plot which takes combination of columns which are having number values.
#it takes the argument for categorical columns (means which has category not a number columns)
#and palette for coloring.
sns.pairplot(dataset,hue= 'sex',palette='dark')
plt.show()