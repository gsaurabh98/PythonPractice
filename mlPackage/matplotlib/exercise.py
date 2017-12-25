import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,100)
y = x*2
z = x**2

#Import matplotlib.pyplot as plt and set %matplotlib inline if you are using the jupyter notebook.
#What command do you use if you aren't using the jupyter notebook?
plt.show()

#Create a figure object called fig using plt.figure()
#Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax.
#Plot (x,y) on that axes and set the labels and titles to match the plot below:
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.plot(x,y)
# plt.show()

#Create a figure object and put two axes on it, ax1 and ax2. Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.

#Now plot (x,y) on both axes. And call your figure object to show it.
#fig = plt.figure()
# ax1 = fig.add_axes([0,0,1,1])
# ax1.plot(x,y)
# ax2 = fig.add_axes([0.2,0.5,0.2,0.2])
# ax2.plot(x,y)
# plt.show()

#Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]
# fig = plt.figure()
# ax1 = fig.add_axes([0,0,1,1])
# ax1.plot(x,z)
# ax1.set_xlabel('X')
# ax1.set_ylabel('Z')
#
# ax2 = fig.add_axes([0.2,0.5,.4,.4])
# ax2.plot(x,y)
# ax2.set_xlabel('X')
# ax2.set_ylabel('Y')
# ax2.set_xlim(20,22)
# ax2.set_ylim(30,50)
# ax2.set_title('zoom')
# plt.show()


#Use plt.subplots(nrows=1, ncols=2) to create the plot below.
# fig,axes = plt.subplots(nrows=1,ncols=2)
# axes[0].plot(x,y,color = 'blue',ls = '--',lw = 3)
# axes[1].plot(x,z,color = 'red',ls = '-',lw = 3)
# plt.show()

#See if you can resize the plot by adding the figsize() argument in plt.subplots()
# are copying and pasting your previous code.
fig,axes = plt.subplots(nrows=1,ncols=2,figsize = (15,3))
axes[0].plot(x,y,color = 'blue',ls = '--',lw = 3)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[1].plot(x,z,color = 'red',ls = '-',lw = 3)
axes[1].set_xlabel('x')
axes[1].set_ylabel('z')
plt.show()
