import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# we have other styles as well, 'bmh', 'dark_background','fivethirtyeight'
plt.style.use('fivethirtyeight')
import pandas as pd

df1 = pd.read_csv('df1', index_col=0)
print df1.head()

df2 = pd.read_csv('df2')
print df2.head()

# we need to pass x and y arguments
df1.plot.line(x=df1.index, y = 'B',figsize = (12,3),lw=1, marker= '*')
plt.show()