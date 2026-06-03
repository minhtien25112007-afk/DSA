def tim_so_chan_dau_tien(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            return i
    return -1


# Nhập mảng
arr = [3, 5, 7, 8, 9]

# Gọi hàm
vi_tri = tim_so_chan_dau_tien(arr)

# In kết quả
if vi_tri != -1:
    print("Số chẵn đầu tiên ở vị trí:", vi_tri)
else:
    print("Mảng không có số chẵn")