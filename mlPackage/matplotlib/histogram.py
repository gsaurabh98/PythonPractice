from matplotlib import pyplot as plt

population_ages = [25,22,36,38,36,3,46,45,48,46,55,55,52,58,55,68,67,61,72,91]
bins = [20,30,40,50,60,70,80,90,100]

plt.hist(population_ages,bins,rwidth= 0.5,histtype='bar')

plt.title("Histogram")
plt.ylabel("Y Axis")
plt.xlabel("X Axis")

# to display the graph
plt.show()