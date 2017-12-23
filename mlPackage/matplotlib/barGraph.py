import numpy as np
from matplotlib import pyplot as plt
#from matplotlib import style # imported for styling the graph

#style.use is used for graph style
#style.use('ggplot')
x = [1,3,5,7,9]
y = [5,1,4,8,10]

a = [2,4,6,8,10]
b = [8,6,2,5,7]

# 'r' used for color, label for legend text , linewidth for line
plt.bar(x,y,color ='c',label = 'Line One')
plt.bar(a,b,label = 'Line Two')

plt.title("Bar Graph")
plt.xlabel("Bar Number")
plt.ylabel("Bar Height")

# used for legend labelling
plt.legend()

# used for plot grid
plt.grid(True,color= 'k')

# to display the graph
plt.show()