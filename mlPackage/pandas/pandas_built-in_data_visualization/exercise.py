import pandas as pd
import matplotlib.pyplot as plt
df3 = pd.read_csv('df3')

print df3.info()
print df3.head()

#Recreate this scatter plot of b vs a. Note the color and size of the points. Also note the figure size.
#See if you can figure out how to stretch it in a similar fashion. Remeber back to your matplotlib lecture...
# df3.plot.scatter(x='a',y ='b',figsize = (12,3),s =50,color = 'red',edgecolors = 'black')
# plt.show()

#Create a histogram of the 'a' column.
# plt.style.use('ggplot')
# df3['a'].plot.hist(bins=30)
# plt.show()

#Create a boxplot comparing the a and b columns.
# df3[['a','b']].plot.box()
# plt.show()

#Create a kde plot of the 'd' column
# df3['d'].plot.kde()
# plt.show()

#Figure out how to increase the linewidth and make the linestyle dashed
# df3['d'].plot.kde(ls='--',lw =5)
# plt.show()

#Create an area plot of all the columns for just the rows up to 30. (hint: use .ix).
# df3.ix[0:30].plot.area(alpha=0.5)
# plt.show()

# print the legend outside
fig = plt.figure()
df3.ix[0:30].plot.area(alpha=0.4)
plt.legend(loc= 'center left', bbox_to_anchor = (1.0,0.5))
plt.show()
