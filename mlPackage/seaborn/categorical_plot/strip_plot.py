import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset = sns.load_dataset('tips')

# strip plot builds the scatter plot based on category takes another argument jitter which generates the noise
#and also takes the hue argument
# based on the hue we can use split or dodge argument as well to split the hue
sns.stripplot(x='day',y ='total_bill',data=dataset, hue='sex',jitter=True, dodge= True)
plt.show()