def bubble_sort_stable(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(arr)

a = [(2,'a'), (1,'b'), (2,'c')]
bubble_sort_stable(a)