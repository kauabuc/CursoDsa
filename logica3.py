lista = [6, 7, 8, 3, 10, 19, 4, 1, 0, 61, 30, 16,
         17, 82, 29, 34, 43, 21, 11, 39, 56, 67, 12]


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


print(bubble_sort(lista))
