def inversion_count(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1

    return count

a = [2, 3, 1]
print("Số nghịch thế:", inversion_count(a))
def bubble_swap_count(arr):
    n = len(arr)
    swaps = 0

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return swaps

a = [2, 3, 1]
print("Số swap:", bubble_swap_count(a))