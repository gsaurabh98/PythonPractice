import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset = sns.load_dataset('tips')

# it combines the violin plot with strip plot to have the better visualization.
# have hue arguement another categorical column, and split to separate the hue
sns.swarmplot(x = 'day', y = 'total_bill',data=dataset, hue = 'sex',dodge=True)

#we can combine the violin plot with swarmplot

sns.violinplot(x="day", y="total_bill", data=dataset,palette='rainbow')
sns.swarmplot(x="day", y="total_bill", data=dataset,color='black',size =3)

plt.show()