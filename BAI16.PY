def min_eating_speed(piles, h):
    left = 1
    right = max(piles)

    while left < right:
        mid = (left + right) // 2

        hours = 0
        for pile in piles:
            hours += (pile + mid - 1) // mid

        if hours <= h:
            right = mid
        else:
            left = mid + 1

    return left

piles = [3, 6, 7, 11]
h = 8

print(min_eating_speed(piles, h))