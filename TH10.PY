def count_passes_needed(arr):
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

    print("Số lượt cần thiết:", passes)

a = [2, 1, 3, 4]
count_passes_needed(a)