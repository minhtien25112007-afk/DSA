def one_pass_bubble(arr):
    n = len(arr)

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    print(arr)

a = [5, 1, 4, 2, 8]
one_pass_bubble(a)