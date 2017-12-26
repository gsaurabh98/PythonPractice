import seaborn as sns
import matplotlib.pyplot as plt

# it comes in built in datasets.
# it works on top of pandas
dataset = sns.load_dataset('tips')
print (dataset.head())

#displot: refers to distribution plot and takes only one column of dataframe essentially a histogram.
#kde : kernel density estimation refers to curve line, by default kde = True
sns.distplot(dataset['total_bill'])

#if we dont want to show the curve line. kde = False
#bins refers to the histogram blocks and depends on datasets

sns.distplot(dataset['total_bill'],kde=False, bins=100)
plt.show()