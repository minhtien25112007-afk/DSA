def bubble_sort_descending(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(arr)

a = [5, 1, 4, 2, 8]
bubble_sort_descending(a)