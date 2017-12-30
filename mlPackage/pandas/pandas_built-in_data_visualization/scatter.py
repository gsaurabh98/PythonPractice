import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# we have other styles as well, 'bmh', 'dark_background','fivethirtyeight'
plt.style.use('ggplot')
import pandas as pd

df1 = pd.read_csv('df1', index_col=0)
print df1.head()

df2 = pd.read_csv('df2')
print df2.head()

# we need to pass x and y arguments, c refers to color, s refers to size , we can use column value
df1.plot.scatter(x= 'A', y = 'B', marker= 'o', c = 'C',s = df1['C']*100,cmap = 'coolwarm')
plt.show()