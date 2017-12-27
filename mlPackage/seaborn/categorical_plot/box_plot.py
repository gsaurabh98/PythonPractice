import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset = sns.load_dataset('tips')

# box plot builds the graph on x axis as categorical column and y as a numerical column.
# it takes another argument called heu which takes another categorical column as a value

#sns.boxplot(x='day',y ='total_bill',data=dataset, hue= 'sex')
#sns.boxplot(x="day", y="total_bill", hue="smoker",data=dataset, palette="coolwarm")

# Can do entire dataframe with orient='h' or 'v'
sns.boxplot(data=dataset,palette='rainbow',orient='h')
plt.show()