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

# df1['A'].hist(bins =30)
# plt.show()

# we can create it an another way.
# df1.plot(kind='hist',bins = 40)
# plt.show()

#we have one more way to create
df1['A'].plot.hist(bins =30)
plt.show()

