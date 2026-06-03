def bubble_sort_length(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(arr)

a = ['abc', 'a', 'ab']
bubble_sort_length(a)