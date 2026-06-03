# Danh sách sinh viên (dạng dictionary)
ds_sinh_vien = [
    {"maSV": "SV01", "hoTen": "Nguyen Van A", "dtb": 8.5},
    {"maSV": "SV02", "hoTen": "Tran Thi B", "dtb": 7.8},
    {"maSV": "SV03", "hoTen": "Le Van C", "dtb": 9.0}
]


# Hàm tìm sinh viên theo mã SV
def tim_sinh_vien(ds, ma_can_tim):
    for sv in ds:
        if sv["maSV"] == ma_can_tim:
            return sv

    return None


# Nhập mã sinh viên cần tìm
ma = input("Nhập mã SV cần tìm: ")

# Gọi hàm
ket_qua = tim_sinh_vien(ds_sinh_vien, ma)

# In kết quả
if ket_qua:
    print("Thông tin sinh viên:")
    print("Mã SV:", ket_qua["maSV"])
    print("Họ tên:", ket_qua["hoTen"])
    print("Điểm TB:", ket_qua["dtb"])
else:
    print("Không tìm thấy sinh viên")