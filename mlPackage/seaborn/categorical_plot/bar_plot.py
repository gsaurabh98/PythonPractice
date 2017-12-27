import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset = sns.load_dataset('tips')
print dataset.head()

#it builds on x axis as a categorical colum and y axis as number value column
#we can put our own function in estimator, by default it takes mean.
#You can change the estimator object to your own function, that converts a vector to a scalar:
sns.barplot(x = 'sex', y = 'total_bill', data=dataset , estimator=np.std)
plt.show()