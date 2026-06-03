def bubble_sort_abs(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if abs(arr[j]) > abs(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(arr)

a = [-3, 1, -2, 2]
bubble_sort_abs(a)