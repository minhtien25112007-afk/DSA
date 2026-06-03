def find_closest_elements(a, k, x):
    left = 0
    right = len(a) - k

    while left < right:
        mid = (left + right) // 2

        if x - a[mid] > a[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return a[left:left + k]

a = [1, 2, 3, 4, 5]
print(find_closest_elements(a, 4, 3))