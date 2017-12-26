import matplotlib.pyplot as plt
import seaborn as sns

dataset = sns.load_dataset('tips')

#rugplots are actually a very simple concept,they just draw a dash mark for every point on a univariate distribution.
#They are the building block of a KDE plot:

sns.rugplot(dataset['total_bill'])
plt.show()