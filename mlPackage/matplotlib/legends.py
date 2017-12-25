import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
y = x**2

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

# labels are used to define the legends
ax.plot(x,x**2,'-r',label = 'X Squared')
ax.plot(x,x**3,'-g',label = 'X Cubed')

#we can specify the legend position by loc argument
# location code 0 refers to best location for the legend and 4 is right lower.
ax.legend(loc = 4)

# we can specify the legend location using tuple.
# the above location will get override
ax.legend(loc = (0.1,0.1))
plt.show()