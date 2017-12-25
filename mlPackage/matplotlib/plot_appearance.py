import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
y = x**3

#for graph appreance we can use below arguments

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])

#for color: use color= 'color_name', we can use  hexcode as well #like FFFFF
#for line width: use linewidth or lw = 'numner'
#for transparency: use alpha = 'number'
#for linestyle like steps (steps),colons(:),dashed(--): use linestyle or ls = ':'
#to mark the points x verses y of all the points: use marker = 'o or + or 1 etc', markersize or ms = 10
#to customize the marker use : markerfacecolor ='color_name', makeredgecolor ='color_name',markeredgewidth = 2

ax.plot(x,y, color = 'red', lw = 1, alpha = 0.5, ls = '-', marker = '*', ms = 20,
        mfc= 'yellow',mew = 2, mec = 'green')
plt.show()