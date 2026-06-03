def analyze_bubble(arr):
    a = arr[:]
    n = len(a)

    compare = 0
    swap = 0

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            compare += 1

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap += 1
                swapped = True

        if not swapped:
            break

    return compare, swap