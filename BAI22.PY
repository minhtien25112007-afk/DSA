def find_median_sorted_arrays(a, b):
    if len(a) > len(b):
        a, b = b, a

    m, n = len(a), len(b)
    left, right = 0, m

    while left <= right:
        cut1 = (left + right) // 2
        cut2 = (m + n + 1) // 2 - cut1

        l1 = float('-inf') if cut1 == 0 else a[cut1 - 1]
        l2 = float('-inf') if cut2 == 0 else b[cut2 - 1]

        r1 = float('inf') if cut1 == m else a[cut1]
        r2 = float('inf') if cut2 == n else b[cut2]

        if l1 <= r2 and l2 <= r1:
            if (m + n) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2
            else:
                return max(l1, l2)

        elif l1 > r2:
            right = cut1 - 1
        else:
            left = cut1 + 1

a = [1, 2]
b = [3, 4]

print(find_median_sorted_arrays(a, b))