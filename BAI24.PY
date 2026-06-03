def minmax_gas_dist(stations, k):
    left = 0
    right = stations[-1] - stations[0]

    while right - left > 1e-6:
        mid = (left + right) / 2

        needed = 0

        for i in range(1, len(stations)):
            gap = stations[i] - stations[i - 1]
            needed += int(gap / mid)

            if gap % mid == 0:
                needed -= 1

        if needed > k:
            left = mid
        else:
            right = mid

    return right

x = [1,2,3,4,5,6,7,8,9,10]
k = 9

print(round(minmax_gas_dist(x, k), 6))