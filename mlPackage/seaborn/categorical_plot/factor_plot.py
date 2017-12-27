import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset = sns.load_dataset('tips')

sns.factorplot(x = 'day', y = 'total_bill',data=dataset)

# we can add another argument called kind which builds the plot accordingly.
sns.factorplot(x = 'day', y = 'total_bill',data=dataset, kind='bar')
plt.show()