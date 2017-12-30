import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris.head())
print iris['species'].unique()

# pairplot is simplified version of pairgrid
#sns.pairplot(iris)

# it will create the empty plot
# first we need to set below into variable
g = sns.PairGrid(iris)
#then we need to map the plot on assigned variable
#suppose scatter plot, we dont need to close the paranthesis inside the map, just need to pass the function name.
#we need to map the grid to plot
#g.map(plt.scatter)

#we can map the other plots on diagonal, upper and lower part of grid
#map_diag will create the displot in diagonal
g.map_diag(sns.distplot)
#map_upper will create the scatter plot above the diagonal
g.map_upper(plt.scatter)
#map_lower will create the kde plot below the diagonal
g.map_lower(sns.kdeplot)


plt.show()