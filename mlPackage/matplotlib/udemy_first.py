import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
y = x**2

# plt.plot(x,y)
# plt.xlabel('X Label')
# plt.ylabel('Y Label')
# plt.title('Title')
# plt.show()

#to plot the subplot in same canvas

# plt.subplot(1,2,1)
# plt.plot(x,y,'r')
# plt.show()
#
# plt.subplot(1,2,2)
# plt.plot(y,x,'g')
# plt.show()

#object Oriented programming for plotting

#first we need to create the figure object then we need to call it.
#add_axes takes 4 arguments ([left,bottom,width,height])
# means % of the blank canvas it takes.

# fig = plt.figure()
# axes = fig.add_axes([0.1,0.1,0.8,0.8])
# axes.plot(x,y)
# axes.set_xlabel('X label')
# axes.set_ylabel('Y label')
# axes.set_title('title')
# plt.show()

#to plot the subplot using OO Method

fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y)
axes1.set_title('Larger Plot')

axes2.plot(y,x)
axes2.set_title('Smaller Plot')

plt.show()