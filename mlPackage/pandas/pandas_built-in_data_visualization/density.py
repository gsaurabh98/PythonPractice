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

#it will create the kde plot or density plot on all the columns or specific columns
df2.plot.pie(y='a')
plt.show()