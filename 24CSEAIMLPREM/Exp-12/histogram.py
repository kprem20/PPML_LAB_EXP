import matplotlib.pyplot as plt
data=[22,87,5,43,56,73,44,56,22,20,51,5]
plt.plot(data)
plt.hist(data,color='purple',label="Histogram data")
plt.title("Histogram ")
plt.legend()
plt.grid()
plt.show()

