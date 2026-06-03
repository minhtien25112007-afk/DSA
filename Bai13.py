def tim_ten(ds, ten_can_tim):
    for i in range(len(ds)):
        if ds[i].lower() == ten_can_tim.lower():
            return i
    return -1


# Danh sách sinh viên
danh_sach = ["An", "Binh", "Lan", "Minh"]

# Nhập tên cần tìm
ten = input("Nhập tên cần tìm: ")

# Gọi hàm tìm kiếm
vi_tri = tim_ten(danh_sach, ten)

# Xuất kết quả
if vi_tri != -1:
    print("Tìm thấy tại vị trí:", vi_tri)
else:
    print("Không tìm thấy")