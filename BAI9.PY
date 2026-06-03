def search_insert(a, x):
    left = 0
    right = len(a)

    while left < right:
        mid = (left + right) // 2

        if a[mid] < x:
            left = mid + 1
        else:
            right = mid

    return left

a = [1, 3, 5, 6]
print(search_insert(a, 4))