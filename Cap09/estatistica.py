import numpy as np

arr = np.array([15, 23, 63, 94, 75])
print(np.mean(arr))
print(np.std(arr))
print(np.var(arr))

arr2 = np.arange(1, 10)
np.prod(arr2)
np.sum(arr2)

arr3 = np.array([1, 2, 3])
arr4 = np.array([3, 2, 1])

print(np.add(arr3, arr4))

arr5 = np.array([[1, 2], [3, 4]])
arr6 = np.array([[5, 6], [0, 7]])
arr7 = np.dot(arr5, arr6)
print(arr7)
