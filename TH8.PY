def check_sorted_after_k(arr, k):
    n = len(arr)

    for i in range(k):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    result = arr == sorted(arr)
    print(result)

a = [3, 2, 1]
k = 1

check_sorted_after_k(a, k)