def tim_max_va_vi_tri(a):
    """
    Hàm tìm giá trị lớn nhất và vị trí của nó trong mảng a.
    Trả về một tuple gồm (gia_tri_lon_nhat, vi_tri).
    Nếu mảng rỗng, trả về (None, -1).
    """
    # Kiểm tra nếu mảng rỗng thì không xử lý
    if len(a) == 0:
        return None, -1
        
    # Bước 1: Khởi tạo giá trị lớn nhất là phần tử đầu tiên
    max_val = a[0]
    max_idx = 0
    
    # Bước 2 & 3: Duyệt tuyến tính từ phần tử thứ hai đến hết mảng
    for i in range(1, len(a)):
        if a[i] > max_val:
            max_val = a[i]  # Cập nhật giá trị lớn nhất mới
            max_idx = i     # Cập nhật vị trí mới
            
    # Bước 4: Trả về kết quả
    return max_val, max_idx

# ==================== CHƯƠNG TRÌNH CHẠY THỬ ====================

# Mảng mẫu thử nghiệm
mang_a = [7, 3, 9, 12, 5, 8, 1]

gia_tri, vi_tri = tim_max_va_vi_tri(mang_a)

print(f"Mảng dữ liệu: {mang_a}")
print(f"-> Giá trị lớn nhất tìm được là: {gia_tri}")  # Kết quả: 12
print(f"-> Vị trí (chỉ số index) của nó là: {vi_tri}") # Kết quả: 3