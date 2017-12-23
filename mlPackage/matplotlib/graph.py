import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style # imported for styling the graph

#style.use is used for graph style
style.use('ggplot')
x = [12,22,-1]
y = [-2,9,11]

a = [15,25,-3]
b = [-6,13,17]

# 'r' used for color, label for legend text , linewidth for line
plt.plot(x,y,'r',label = 'Line One',linewidth = 3)
plt.plot(a,b,'b',label = 'Line Two',linewidth = 3)

plt.title("Graph Info")
plt.ylabel("Y Axis")
plt.xlabel("X Axis")

# used for legend labelling
plt.legend()

# used for plot grid
plt.grid(True,color= 'k')

# to display the graph
plt.show()