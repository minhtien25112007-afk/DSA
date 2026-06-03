# Tìm kiếm tuyến tính thông thường
def tim_kiem_thuong(arr, x):
    so_sanh = 0

    for i in range(len(arr)):
        so_sanh += 1
        if arr[i] == x:
            return i, so_sanh

    return -1, so_sanh


# Tìm kiếm lính canh (Sentinel)
def tim_kiem_linh_canh(arr, x):
    n = len(arr)

    # Thêm lính canh
    arr.append(x)

    i = 0
    so_sanh = 0

    while arr[i] != x:
        so_sanh += 1
        i += 1

    so_sanh += 1

    # Xóa lính canh
    arr.pop()

    if i < n:
        return i, so_sanh
    else:
        return -1, so_sanh


# Ví dụ
arr = [5, 8, 12, 20, 7]
x = 20

# Gọi 2 cách tìm kiếm
vt1, ss1 = tim_kiem_thuong(arr, x)
vt2, ss2 = tim_kiem_linh_canh(arr, x)

print("Tìm kiếm thông thường:")
print("Vị trí:", vt1)
print("Số phép so sánh:", ss1)

print("\nTìm kiếm lính canh:")
print("Vị trí:", vt2)
print("Số phép so sánh:", ss2)