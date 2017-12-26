import matplotlib.pyplot as plt
import seaborn as sns

dataset = sns.load_dataset('tips')

sns.kdeplot(dataset['total_bill'])
sns.rugplot(dataset['total_bill'])
plt.show()