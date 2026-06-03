def min_passes(initial, target):
    a = initial[:]
    n = len(a)

    if a == target:
        return 0

    for p in range(1, n + 1):

        # Thực hiện 1 lượt Bubble Sort
        for j in range(n - p):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

        if a == target:
            return p

    return -1  # Không thể tạo ra trạng thái này


initial = [4, 3, 2, 1]
target = [3, 2, 1, 4]

print("Số lượt tối thiểu:", min_passes(initial, target))