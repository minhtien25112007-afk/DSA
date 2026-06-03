def partial_bubble_sort(arr, k):
    n = len(arr)

    for i in range(k):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

a = [3, 1, 4, 1, 5]
k = 2

print(partial_bubble_sort(a, k))