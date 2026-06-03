def one_pass_bubble(arr):
    n = len(arr)

    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("Phần tử cuối sau 1 lượt:", arr[n - 1])

a = [4, 2, 7, 1, 3]
one_pass_bubble(a)