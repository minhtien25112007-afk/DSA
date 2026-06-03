def ship_within_days(weights, D):
    left = max(weights)
    right = sum(weights)

    while left < right:
        mid = (left + right) // 2

        days = 1
        current = 0

        for w in weights:
            if current + w > mid:
                days += 1
                current = 0

            current += w

        if days <= D:
            right = mid
        else:
            left = mid + 1

    return left

w = [1,2,3,4,5,6,7,8,9,10]
D = 5

print(ship_within_days(w, D))