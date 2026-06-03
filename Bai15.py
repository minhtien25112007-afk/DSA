# Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# Hàm tìm số nguyên tố đầu tiên
def tim_so_nguyen_to_dau_tien(arr):
    for i in range(len(arr)):
        if la_so_nguyen_to(arr[i]):
            return arr[i], i

    return -1, -1


# Mảng ví dụ
arr = [4, 8, 10, 11, 15]

# Gọi hàm
gia_tri, vi_tri = tim_so_nguyen_to_dau_tien(arr)

# In kết quả
if vi_tri != -1:
    print("Số nguyên tố đầu tiên là:", gia_tri)
    print("Vị trí:", vi_tri)
else:
    print("Không có số nguyên tố trong mảng")