import numpy as np

arr = np.array([10, 21, 32, 43, 48, 15, 76, 57, 89])
mask = (arr % 2 == 0)
indices = [1, 2, 6, 5]
print(arr[4])
print(arr[1:4+1])
print(arr[indices])
print(arr[mask])


arr2 = np.array([1, 2, 3, 4, 5])
print(arr2.cumsum())
print(arr2.cumprod())

arr3 = np.arange(0, 50, 5)
print(arr3)

arr4 = np.zeros(10)
print(arr4)


arr5 = np.eye(3)
print(arr5)

arr6 = np.diag(np.array([1, 2, 3, 4]))
print(arr6)

arr7 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr7)

arr8 = np.ones((2, 3))
print(arr8)

lista = [[13, 22, 81], [0, 34, 59], [21, 48, 93]]
arr9 = np.matrix(lista)

print(arr9[2, 1])
print(arr9[0:2, 1])
arr9[1, 0] = 100
print(arr9)
