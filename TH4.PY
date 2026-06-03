def count_swaps_bubble(arr):
    n = len(arr)
    swaps = 0

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    print("Mảng sau sắp xếp:", arr)
    print("Số lần hoán đổi:", swaps)

a = [3, 2, 1]
count_swaps_bubble(a)