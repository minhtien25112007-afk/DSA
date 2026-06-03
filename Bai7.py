def ton_tai(a, x):
    """
    Hàm kiểm tra sự tồn tại của x trong mảng a.
    Trả về True nếu tìm thấy x, ngược lại trả về False.
    """
    for phan_tu in a:
        if phan_tu == x:
            return True  # Tìm thấy x, lập tức trả về True và dừng hàm
            
    return False  # Đã duyệt hết mảng mà không gặp x, trả về False

# ==================== CHƯƠNG TRÌNH CHẠY THỬ ====================

# Mảng mẫu để kiểm tra
mang_A = [7, 3, 9, 12, 5, 8, 1]

# Trường hợp 1: Phần tử có tồn tại
x1 = 5
print(f"Kiểm tra {x1}: {ton_tai(mang_A, x1)}")  # Kết quả: True

# Trường hợp 2: Phần tử không tồn tại
x2 = 100
print(f"Kiểm tra {x2}: {ton_tai(mang_A, x2)}")  # Kết quả: False