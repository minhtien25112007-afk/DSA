def split_array(nums, k):
    left = max(nums)
    right = sum(nums)

    while left < right:
        mid = (left + right) // 2

        parts = 1
        current = 0

        for num in nums:
            if current + num > mid:
                parts += 1
                current = num
            else:
                current += num

        if parts <= k:
            right = mid
        else:
            left = mid + 1

    return left

a = [7, 2, 5, 10, 8]
k = 2

print(split_array(a, k))