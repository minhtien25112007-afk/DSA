def bubble_early(arr):
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

    return passes

a = [1,3,2,4,6,5]
print(bubble_early(a))