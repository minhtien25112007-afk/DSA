def allocate_books(pages, m):
    if m > len(pages):
        return -1

    left = max(pages)
    right = sum(pages)

    while left < right:
        mid = (left + right) // 2

        students = 1
        current = 0

        for page in pages:
            if current + page > mid:
                students += 1
                current = page
            else:
                current += page

        if students <= m:
            right = mid
        else:
            left = mid + 1

    return left

p = [12, 34, 67, 90]
m = 2

print(allocate_books(p, m))