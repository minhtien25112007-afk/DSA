def bubble_sort_early_exit(arr):
    n = len(arr)
    passes = 0

    for i in range(n):
        swapped = False
        passes += 1

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    print("Số lượt chạy:", passes)

a = [1, 2, 3, 4]
bubble_sort_early_exit(a)