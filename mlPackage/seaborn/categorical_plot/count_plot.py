import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset = sns.load_dataset('tips')

#This is essentially the same as barplot except the estimator is explicitly counting the number of occurrences.
#Which is why we only pass the x value:

sns.countplot(x = 'sex',data=dataset)
plt.show()