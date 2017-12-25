import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
y = x**2

#fig size and dpi are arguments which passes in figure and subplot methods
#fig size takes the width and height as tuple parameter and dpi (dots or pixel per inch)

fig = plt.figure(figsize=(3,2),dpi=200)
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y)


figs,ax = plt.subplots(nrows=2,ncols=1,figsize= (8,2),dpi = 100)
ax[0].plot(x,y)
ax[0].set_label('Upper Plot')

ax[1].plot(y,x)
ax[1].set_label('Upper Plot')
plt.tight_layout()
plt.show()