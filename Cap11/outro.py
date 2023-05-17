import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
y = [6, 7, 8, 2, 4]

# plt.plot(x, y, label="Graficos com Matplot")
# plt.legend()

# plt.bar(x, y, label="Barras", color="green")
# plt.legend()
# plt.show()

x1 = [1, 3, 5, 7, 9]
y1 = [7, 8, 2, 4, 2]
plt.bar(x, y, label="Lista 1", color="blue")
plt.bar(x1, y1, label="Lista 2", color="red")
plt.legend()
plt.show()

# plt.hist
