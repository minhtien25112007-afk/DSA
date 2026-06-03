def merge_count(left, right):
    merged = []
    i = j = 0
    inv = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inv


def inversion_count(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    left, inv_left = inversion_count(arr[:mid])
    right, inv_right = inversion_count(arr[mid:])

    merged, inv_merge = merge_count(left, right)

    return merged, inv_left + inv_right + inv_merge


a = [2, 3, 1]

_, inversions = inversion_count(a)

print("Số swap =", inversions)