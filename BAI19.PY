def aggressive_cows(x, c):
    x.sort()

    left = 1
    right = x[-1] - x[0]

    while left <= right:
        mid = (left + right) // 2

        count = 1
        last = x[0]

        for i in range(1, len(x)):
            if x[i] - last >= mid:
                count += 1
                last = x[i]

        if count >= c:
            left = mid + 1
        else:
            right = mid - 1

    return right

x = [1, 2, 4, 8, 9]
c = 3

print(aggressive_cows(x, c))