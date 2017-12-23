from matplotlib import pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,9,6,11,5]
eating = [2,3,4,5,2]
playing = [5,8,3,6,1]
working = [8,5,7,8,13]

plt.plot([],[],color='m', label='sleeping',linewidth = 5)
plt.plot([],[],color='c', label='eating',linewidth = 5)
plt.plot([],[],color='r', label='playing',linewidth = 5)
plt.plot([],[],color='k', label='working',linewidth = 5)

plt.stackplot(days,sleeping,eating,playing,working,colors= ['m','c','r','k'])

plt.title("Stack or Area Plot")
plt.ylabel("Y Axis")
plt.xlabel("X Axis")

plt.legend()
# to display the graph
plt.show()