import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset = sns.load_dataset('tips')

#violin plots are same as box plot and there is one more argument split which sets to True for combining the
#hue else False, bydefault it sets to False
#palette used for coloring
sns.violinplot(x ='day', y = 'total_bill',data= dataset,hue = 'sex', split=True,palette='Set1')
plt.show()
