import os

import numpy as np

arr_3d = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [
                  [13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]])

print(arr_3d)

filename = os.path.join("pytohn/Cursodsa/Cap09/dataset.csv")
arr2 = np.loadtxt(filename, delimiter=",", usecols=(0, 1, 2, 3), skiprows=1)

var1, var2 = np.loadtxt(filename, delimiter=",",
                        usecols=(0, 1), skiprows=1, unpack=True)
