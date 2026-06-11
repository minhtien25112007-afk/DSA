def binary_search(a, key, left, right):

    while left <= right:

        mid = (left + right) // 2

        if a[mid] > key:
            right = mid - 1
        else:
            left = mid + 1

    return left
a = [5, 2, 4, 6, 1, 3]

compare = 0

for i in range(1, len(a)):

    key = a[i]

    pos = binary_search(a, key, 0, i - 1)

    j = i - 1

    while j >= pos:
        a[j + 1] = a[j]
        j -= 1

    a[pos] = key

print(a)