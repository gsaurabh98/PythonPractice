import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

#we can set the styling using set_style method.
#sns.set_style('whitegrid') # it will set the backgroud white and make the lines
sns.set_style('ticks') # it will create the edges on border
# we can resize the graph using matplotlib figsize.
plt.figure(figsize=(12,3)) # as this will override the seaborn plot size though it writter before seaborn plot.
# it will set the size for seaborn plot.

# we can resize it usinf aspect and size parmeter in seaborn
#sns.lmplot(x='total_bill',y='tip',size=2,aspect=4,data=tips) #just a example.

#we can set the context and font_scale means , how we want the plot to be displayed.
sns.set_context('poster', font_scale=3)

sns.countplot(x = 'sex' , data = tips, palette='seismic')

# despine mathod will remove the border
sns.despine(left=True,bottom=True) # bydefault top and right set to True, we can remove left and bottom as well.

plt.show()

