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

#it will create the box plot on two columns x,y , we can chnage the hexbin size using gridsize argument.
df1.plot.hexbin(x='A',y='B',gridsize = 30)
plt.show()