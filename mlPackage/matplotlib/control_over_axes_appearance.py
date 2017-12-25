import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
y = x**2

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])


# we can restrict the plotting into x and y axis (control axis sizing)
# by using set_xlim(lowerbound,upperbound) using tuple and list
ax.plot(x,y, ls = '-',lw = 2)
ax.set_xlim(0,1)
ax.set_ylim(0,2)
plt.show()