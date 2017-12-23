from matplotlib import pyplot as plt

x = [25,22,36,38,36,23,46,45,48]
y = [20,30,40,50,60,70,80,90,10]

plt.scatter(x,y,color='k', label='scatter')

plt.title("Scatter")
plt.ylabel("Y Axis")
plt.xlabel("X Axis")

plt.legend()
# to display the graph
plt.show()