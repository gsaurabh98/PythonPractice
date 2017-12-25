import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,5,11)
y = x**2

# plotting the subgraph
#fig,axes = plt.subplots()
#plt.show()

# plotting the multiple subplots based on rows and columns
# fig,axes = plt.subplots(nrows=3,ncols=3)
#
# # to fix the overlapping issue
# axes[0,1].plot(x,y)
# plt.tight_layout()
# plt.show()

#axes variable is basically a list here , we can iterate over it.
# fig,axes = plt.subplots(nrows=3,ncols=3)
# for current_ax in axes:
#     current_ax.plot(x,y)
# plt.show()

#though axes are list so we can use indexing also.
#tuple unpacking
fig,axes = plt.subplots(nrows=1,ncols=2)
axes[0].plot(x,y)
axes[0].set_title('First Plot')

axes[1].plot(y,x)
axes[1].set_title('Second Plot')
plt.tight_layout()
plt.show()

