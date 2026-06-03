def bubble_sort_count_compare(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            count += 1      # đếm số lần so sánh

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("Mảng sau sắp xếp:", arr)
    print("Số lần so sánh:", count)

a = [1, 2, 3]
bubble_sort_count_compare(a)