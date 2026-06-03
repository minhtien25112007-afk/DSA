# Hàm tìm kiếm trong ma trận 2 chiều
def tim_kiem_ma_tran(matrix, x):
    for i in range(len(matrix)):          # duyệt từng dòng
        for j in range(len(matrix[i])):  # duyệt từng cột
            if matrix[i][j] == x:
                return i, j

    return -1, -1


# Ma trận ví dụ
matrix = [
    [1, 5, 7],
    [8, 10, 12],
    [15, 20, 25]
]

x = 10

# Gọi hàm
dong, cot = tim_kiem_ma_tran(matrix, x)

# In kết quả
if dong != -1:
    print("Tìm thấy tại vị trí:")
    print("Dòng:", dong)
    print("Cột:", cot)
else:
    print("Không tìm thấy")