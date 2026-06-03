def search_matrix(matrix, x):
    m = len(matrix)
    n = len(matrix[0])

    left = 0
    right = m * n - 1

    while left <= right:
        mid = (left + right) // 2

        row = mid // n
        col = mid % n

        if matrix[row][col] == x:
            return True
        elif matrix[row][col] < x:
            left = mid + 1
        else:
            right = mid - 1

    return False

matrix = [
    [1, 3, 5],
    [7, 9, 11]
]

print(search_matrix(matrix, 9))